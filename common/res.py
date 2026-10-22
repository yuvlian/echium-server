from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from .util import AsyncFs

FILE_DIR = "./common/res"


class AvatarConfig(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    weakness_buff_id: int
    technique_buff_ids: list[int]


class AvatarConfigs(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    avatar_configs: dict[int, AvatarConfig]


class ExEidolonConfig(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: int
    status_id: int
    name: str = ""


class ExEidolons(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    ex_eidolons: dict[int, list[ExEidolonConfig]]


AVATAR_CONFIGS: dict[int, AvatarConfig] = {}
EX_EIDOLON_CONFIGS: dict[int, list[ExEidolonConfig]] = {}
EX_EIDOLON_NAMES: dict[int, str] = {}
_loaded = False


async def load_res():
    global _loaded
    if not _loaded:
        k, _ = await AsyncFs.json_parse_or_write(
            f"{FILE_DIR}/avatarConfigs.json",
            AvatarConfigs,
            AvatarConfigs(avatar_configs={}),
            False,
        )
        AVATAR_CONFIGS.update(k.avatar_configs)

        k, _ = await AsyncFs.json_parse_or_write(
            f"{FILE_DIR}/exEidolons.json",
            ExEidolons,
            ExEidolons(ex_eidolons={}),
            False,
        )
        EX_EIDOLON_CONFIGS.update(k.ex_eidolons)
        EX_EIDOLON_NAMES.update(
            {aid: cfgs[0].name for aid, cfgs in k.ex_eidolons.items() if cfgs}
        )
        _loaded = True
