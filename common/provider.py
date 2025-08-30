import starkbank

from common.settings import settings


def get_starkbank():
    project = starkbank.Project(
        environment=settings.enviroment,
        id=settings.stark_project_id,
        private_key=settings.private_key
    )
    starkbank.user = project