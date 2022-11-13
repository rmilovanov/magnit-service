from fastapi.testclient import TestClient
import pytest
import mock

from service.main import app


client = TestClient(app)


@pytest.mark.parametrize(
    "case",
    (
        {"json": {"x": 3, "y": 5, "operation": "+"}, "status_code": 200},
        {"json": {"x": 3, "y": 5, "operation": "!"}, "status_code": 422},
    ),
)
def test_post_calc(monkeypatch, case):
    from service import main

    class MockTask:
        id = "test_task_id"

    monkeypatch.setattr(
        main.make_computations, "delay", mock.MagicMock(return_value=MockTask)
    )

    response = client.post(
        "/calc/",
        json=case["json"],
    )

    assert response.status_code == case["status_code"]
    if response.status_code == 200:
        assert response.json() == {"id": "test_task_id"}
    else:
        assert (
            response.json()["detail"][0]["msg"]
            == "Supported operations are ['+', '-', '*', '/']"
        )


def test_get_task_result(monkeypatch):
    from service import main

    class MockTaskResult:
        status = "SUCCESS"
        result = 124

    # tasks_mock = mock.MagicMock(return_value={"test_task_id1": {"status": "ready", "result": 124}})
    monkeypatch.setattr(
        main, "AsyncResult", mock.MagicMock(return_value=MockTaskResult)
    )

    response = client.get("/task/test_task_id1/")
    assert response.status_code == 200
    assert response.json() == {
        "task_id": "test_task_id1",
        "task_result": 124,
        "task_status": "SUCCESS",
    }
