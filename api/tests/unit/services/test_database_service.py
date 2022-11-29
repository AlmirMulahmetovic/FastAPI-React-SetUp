from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from services.database import DatabaseService


class TestDatabaseService:
    @pytest.mark.asyncio
    @patch("services.database.SessionLocal")
    async def test_db_session_middleware(self, session_local_mock):
        return_value = await DatabaseService.db_session_middleware(
            request_mock := MagicMock(), call_next_mock := AsyncMock()
        )

        assert request_mock.state.db == session_local_mock.return_value
        call_next_mock.assert_called_once_with(request_mock)
        request_mock.state.db.close.assert_called_once()
        assert return_value == call_next_mock.return_value

    @pytest.mark.asyncio
    @patch("services.database.SessionLocal")
    async def test_db_session_middleware_handles_errors(self, session_local_mock):
        with pytest.raises(Exception):
            await DatabaseService.db_session_middleware(
                request_mock := MagicMock(), call_next_mock := AsyncMock(side_effect=Exception)
            )

        assert request_mock.state.db == session_local_mock.return_value
        call_next_mock.assert_called_once_with(request_mock)
        request_mock.state.db.close.assert_called_once()

    def test_get_db_session(self):
        assert DatabaseService.get_db_session(request_mock := MagicMock()) == request_mock.state.db
