import pytest
from server.MockServer import MockServer
mockserver = MockServer()

class TestMockServer:
    def test_200_status(self):
        result = mockserver.Get200Code()
        assert result.status_code == 200


    def test_400_status(self):
        result = mockserver.Get400Code()
        assert result.status_code == 400


    def test_500_status(self):
        result = mockserver.Get500Code()
        assert result.status_code == 500

    #@pytest.mark.skip("XFAILED")
    def test_200_xfailed(self):
        result = mockserver.Get500Code()
        assert result.status_code == 200

    @pytest.mark.skip("XFAILED")
    def test_200_failed(self):
        result = mockserver.Get500Code()
        assert result.status_code == 200
