class ScenarioParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        # Basic parser: Each line is treated as a scene
        scenes = []
        with open(self.file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    scenes.append({"scene": line})
        return scenes
