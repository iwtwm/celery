from unittest.mock import patch

from t.unit import conftest
from celery.app.utils import Settings


class test_worker:
    def test_worker_on_start_all_true(self):
        worker = self.app.Worker()
        worker.purge = True
        worker.quiet = True
        worker._custom_logging = False
        worker.redirect_stdouts = True
        self.app._config_source = "some_config_source"
        
        with conftest.stdouts():
            with patch.object(Settings, 'maybe_warn_deprecated_settings') as mocked_maybe_warn_deprecated_settings:
                mocked_maybe_warn_deprecated_settings.return_value = True
                worker.on_start()
                assert worker.startup_info()
    
    def test_worker_on_start_all_false(self):
        worker = self.app.Worker()
        worker.purge = False
        worker.quiet = False
        worker._custom_logging = True
        worker.redirect_stdouts = False
        self.app._config_source = None
        
        with conftest.stdouts():
            with patch.object(Settings, 'maybe_warn_deprecated_settings') as mocked_maybe_warn_deprecated_settings:
                mocked_maybe_warn_deprecated_settings.return_value = False
                worker.on_start()
                assert worker.startup_info()