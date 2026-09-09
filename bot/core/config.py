from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    TOKEN: str
    DEV_GUILD_ID: int | None = None
    WELCOME_CHANNEL_ID: int | None = None
    RULES_INFO_ID: int | None = None
    
    BAHASA_ROLE : int | None = None
    MANGA_ROLE : int | None = None
    COSPLAY_ROLE : int | None = None
    
    ANG_2020_ROLE: int | None = None
    ANG_2021_ROLE: int | None = None
    ANG_2022_ROLE: int | None = None
    ANG_2023_ROLE: int | None = None
    ANG_2024_ROLE: int | None = None
    ANG_2025_ROLE: int | None = None
    ANG_2026_ROLE: int | None = None

    
    FEB_ROLE: int | None = None
    FH_ROLE: int | None = None
    FT_ROLE: int | None = None
    FAPRE_ROLE: int | None = None
    FK_ROLE: int | None = None
    FPSI_ROLE: int | None = None
    FSRD_ROLE: int | None = None
    FTI_ROLE: int | None = None
    FIKOM_ROLE: int | None = None
    
    SHE_HER_ROLE: int | None = None
    HE_HIM_ROLE: int | None = None
    THEY_THEM_ROLE: int | None = None
    ASK_PRONOUNS_ROLE: int | None = None
    
    DMS_OPEN_ROLE: int | None = None
    DMS_CLOSED_ROLE: int | None = None
    ASK_TO_DM_ROLE: int | None = None
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()