import hashlib
import json


A = "Study A. Method: randomized 100 subjects. Measured result: intervention increased recovery."
B = "Study B. Method: randomized 120 subjects. Measured result: intervention increased recovery."


def h(text):
    return hashlib.sha256(text.encode()).hexdigest()


def prepare(c, vm, owner):
    vm.sender = owner
    c.open_panel("recovery", "Does intervention X improve recovery in adults?",
                 "Compare randomized adult trials measuring recovery at 30 days.")
    c.submit_study("recovery", "a", "https://alpha.example.org/study", h(A))
    c.submit_study("recovery", "b", "https://beta.example.net/study", h(B))
    vm.mock_web(r"alpha\.example\.org/study", {"status": 200, "body": A})
    vm.mock_web(r"beta\.example\.net/study", {"status": 200, "body": B})


def test_convergent_report(direct_vm, direct_deploy, direct_alice):
    c = direct_deploy("contracts/ReplicationConvergencePanel.py")
    prepare(c, direct_vm, direct_alice)
    direct_vm.mock_llm(r".*Study A.*", json.dumps({"comparable": True, "direction": "POSITIVE"}))
    direct_vm.mock_llm(r".*Study B.*", json.dumps({"comparable": True, "direction": "POSITIVE"}))
    c.assess("recovery", "first")
    report = json.loads(c.get_snapshot("recovery", "first"))
    assert report["decision"] == "CONVERGENT"
    assert report["eligible_count"] == 2
    with direct_vm.expect_revert("new evidence required"):
        c.assess("recovery", "again")


def test_disputed_report(direct_vm, direct_deploy, direct_alice):
    c = direct_deploy("contracts/ReplicationConvergencePanel.py")
    prepare(c, direct_vm, direct_alice)
    direct_vm.mock_llm(r".*Study A.*", json.dumps({"comparable": True, "direction": "POSITIVE"}))
    direct_vm.mock_llm(r".*Study B.*", json.dumps({"comparable": True, "direction": "NEGATIVE"}))
    c.assess("recovery", "first")
    assert json.loads(c.get_panel("recovery"))["state"] == "DISPUTED"


def test_hash_mismatch_and_duplicate_authority_fail_closed(direct_vm, direct_deploy, direct_alice):
    c = direct_deploy("contracts/ReplicationConvergencePanel.py")
    prepare(c, direct_vm, direct_alice)
    with direct_vm.expect_revert("unique study and hostname required"):
        c.submit_study("recovery", "c", "https://alpha.example.org/other", h(A))
    direct_vm.clear_mocks()
    direct_vm.mock_web(r"alpha\.example\.org/study", {"status": 200, "body": A})
    direct_vm.mock_web(r"beta\.example\.net/study", {"status": 200, "body": "tampered"})
    direct_vm.mock_llm(r".*Study A.*", json.dumps({"comparable": True, "direction": "POSITIVE"}))
    c.assess("recovery", "bad")
    report = json.loads(c.get_snapshot("recovery", "bad"))
    assert report["decision"] == "INCONCLUSIVE"
    assert report["entries"][1]["source"]["hash_match"] is False
