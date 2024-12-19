from random import choices
from string import ascii_uppercase, ascii_letters, digits
from typing import List, Dict, Any, AsyncGenerator


class IssueHotline:
    MAX_STACK = 100
    """
    Hotline issue class.
    """
    async def __generate_code(self) -> str:
        part1 = "".join(choices(ascii_uppercase, k=2))
        part2 = "".join(choices(ascii_letters + digits, k=4))
        part3 = "".join(choices(ascii_letters + digits, k=4))
        return f"{part1}-{part2}-{part3}"

    async def __generate_count(
        self,
        items_list: List[Dict[str, Any]]
    ) -> AsyncGenerator[Dict[str, Any], None]:

        for item in items_list:
            item_count = item.get("m_count", 0)
            item_name = item.get("m_item", "")
            full_stacks, remainder = divmod(item_count, self.MAX_STACK)

            for _ in range(full_stacks):
                yield {"m_item": item_name, "m_count": self.MAX_STACK}

            if remainder > 0:
                yield {"m_item": item_name, "m_count": remainder}

    async def create_items(
        self,
        issue_name: str,
        items_list: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Create a dictionary with generated codes and processed items.

        items_list example: [{"m_item": "item1", "m_count": 10}, {"m_item": "item2", "m_count": 20}]
        """
        processed_items = [item async for item in self.__generate_count(items_list)]
        return {
            "m_CodeArray": [
                {
                    "m_code": await self.__generate_code(),
                    "m_name": issue_name,
                    "m_type": "item",
                    "m_itemsArray": processed_items,
                    "m_teleport_position": "",
                    "m_vehicles": {
                        "m_item": "",
                        "m_attachments": [],
                        "m_cargo": []
                    },
                    "m_give_zone_positions": [],
                    "m_give_zone_positions_forbidden": [],
                }
            ]
        }

    async def create_vehicle(
        self,
        issue_name: str,
        items_dict: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Create a dictionary with generated code and vehicle data.

        items_dict example: {"m_item": "class_name", "m_attachments": ["class_name"], "m_cargo": null}
        """
        return {
            "m_CodeArray": [
                {
                    "m_code": await self.__generate_code(),
                    "m_name": issue_name,
                    "m_type": "vehicle",
                    "m_itemsArray": [],
                    "m_teleport_position": "",
                    "m_vehicles": items_dict,
                    "m_give_zone_position": "",
                    "m_give_zone_radius": 0,
                    "m_give_zone_positions": [],
                    "m_give_zone_positions_forbidden": [],
                    "m_fresh_spawn_delay": 0
                }
            ]
        }

    async def create_teleport(
        self,
        issue_name: str,
        teleport_position: str
    ) -> Dict[str, Any]:
        """
        Create a dictionary with generated code and teleport data.

        teleport_position format: (x, y, z)
        """
        return {
            "m_CodeArray": [
                {
                    "m_code": await self.__generate_code(),
                    "m_name": issue_name,
                    "m_type": "teleport",
                    "m_itemsArray": [],
                    "m_teleport_position": teleport_position,
                    "m_vehicles": {
                        "m_item": "",
                        "m_attachments": []
                    },
                    "m_give_zone_position": "",
                    "m_give_zone_radius": 0,
                    "m_fresh_spawn_delay": 0
                }
            ]
        }
