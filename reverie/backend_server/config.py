"""
Configuration module using PydanticSettings for environment variable management.
"""
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent.parent / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    openai_api_key: str
    key_owner: str = "User"
    
    collision_block_id: str = "32125"
    debug: bool = True

    @property
    def maze_assets_loc(self) -> str:
        return str(Path(__file__).parent.parent.parent / "environment" / "frontend_server" / "static_dirs" / "assets")

    @property
    def env_matrix(self) -> str:
        return f"{self.maze_assets_loc}/the_ville/matrix"

    @property
    def env_visuals(self) -> str:
        return f"{self.maze_assets_loc}/the_ville/visuals"

    @property
    def fs_storage(self) -> str:
        return str(Path(__file__).parent.parent.parent / "environment" / "frontend_server" / "storage")

    @property
    def fs_temp_storage(self) -> str:
        return str(Path(__file__).parent.parent.parent / "environment" / "frontend_server" / "temp_storage")


settings = Settings()

openai_api_key = settings.openai_api_key
key_owner = settings.key_owner
maze_assets_loc = settings.maze_assets_loc
env_matrix = settings.env_matrix
env_visuals = settings.env_visuals
fs_storage = settings.fs_storage
fs_temp_storage = settings.fs_temp_storage
collision_block_id = settings.collision_block_id
debug = settings.debug

