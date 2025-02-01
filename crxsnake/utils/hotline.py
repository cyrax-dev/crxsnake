from random import choices
from dataclasses import dataclass, field
from string import ascii_uppercase, ascii_letters, digits
from typing import List, Dict, Any, Generator


@dataclass
class CodeArray:
    m_code: str
    m_name: str
    m_type: str
    m_itemsArray: List[Dict[str, Any]] = field(default_factory=list)
    m_teleport_position: str = ""
    m_vehicles: Dict[str, Any] = field(default_factory=lambda: {"m_item": "", "m_attachments": [], "m_cargo": []})
    m_give_zone_positions: List[Dict[str, Any]] = field(default_factory=list)
    m_give_zone_positions_forbidden: List[Dict[str, Any]] = field(default_factory=list)


class IssueHotline:
    MAX_STACK = 100

    @staticmethod
    def __generate_code() -> str:
        return "-".join([
            "".join(choices(ascii_uppercase, k=2)),
            "".join(choices(ascii_letters + digits, k=4)),
            "".join(choices(ascii_letters + digits, k=4))
        ])

    def __generate_count(self, items_list: List[Dict[str, Any]]) -> Generator[Dict[str, Any], None, None]:
        for item in items_list:
            item_count = item.get("m_count", 0)
            item_name = item.get("m_item", "")
            full_stacks, remainder = divmod(item_count, self.MAX_STACK)

            for _ in range(full_stacks):
                yield {"m_item": item_name, "m_count": self.MAX_STACK}

            if remainder > 0:
                yield {"m_item": item_name, "m_count": remainder}

    async def create_items(self, issue_name: str, items_list: List[Dict[str, Any]]) -> Dict[str, Any]:
        processed_items = [item for item in self.__generate_count(items_list)]
        return {"m_CodeArray": [CodeArray(
            m_code=self.__generate_code(),
            m_name=issue_name,
            m_type="item",
            m_itemsArray=processed_items
        ).__dict__]}

    async def create_vehicle(self, issue_name: str, items_dict: Dict[str, Any]) -> Dict[str, Any]:
        return {"m_CodeArray": [CodeArray(
            m_code=self.__generate_code(),
            m_name=issue_name,
            m_type="vehicle",
            m_vehicles=items_dict
        ).__dict__]}

    async def create_teleport(self, issue_name: str, teleport_position: str) -> Dict[str, Any]:
        return {"m_CodeArray": [CodeArray(
            m_code=self.__generate_code(),
            m_name=issue_name,
            m_type="teleport",
            m_teleport_position=teleport_position
        ).__dict__]}
