from taskTracker import settings

def test_secret_key():
    assert not hasattr(settings.base, 'SECRET_KEY'), "SECRET_KEY should not be in base settings"
    assert hasattr(settings.local, 'SECRET_KEY'), "SECRET_KEY should be in local settings"

def test_gitignore_local():
    with open(".gitignore") as gi:
        lines = gi.readlines()
        assert "taskTracker/settings/local.py\n" in lines, "*local.py* must be git-ignored"