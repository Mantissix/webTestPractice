import yaml

from pageObject.pagePackage.home_page import HomePage


class TestAddMember:
    def setup(self):
        self.main = HomePage()

    def teatdown(self):

        pass

    def test_contact_addmember(self):
        with open("../memberData/memberData", encoding="utf-8") as member:
            members = yaml.safe_load(member)
        name = members["name"]
        memberId = members["id"]
        phone = members["phone"]
        ele = self.main.goto_contact().click_add_ember().addMembers(name, memberId, phone).get_members()
        assert phone in ele

    def test_addmember(self):
        ele = self.main.goto_add()

