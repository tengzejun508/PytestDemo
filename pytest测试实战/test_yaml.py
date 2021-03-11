import yaml


class YamlDemo():
    def getDatas(self):
        with open("./data.yml") as f:
            self.result = yaml.safe_load(f)
            self.datas = self.result["datas"]
            self.ids = self.result["ids"]
            return [self.datas, self.ids]

    # def test_demo(self):
    #     self.test = TestYaml()
    #     print(self.test.getDatas())