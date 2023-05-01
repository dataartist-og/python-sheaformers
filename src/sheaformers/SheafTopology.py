class SheafTopology:
    def __init__(self, space, overlap_func, local_func):
        self.space = space
        self.overlap_func = overlap_func
        self.local_func = local_func
        self._global_sections = None

    def overlap(self, open_sets):
        return self.overlap_func(open_sets)

    def sections(self, open_set):
        seeds = self.local_func(open_set)
        section = set()
        for seed in seeds:
            section.add(seed.intersection(open_set))
        return section

    def stalk(self, point):
        sections = self.sections(point)
        quotient = {}
        for seed in sections:
            if point in seed:
                quotient[seed.germ] = [edge[1] for edge in seed.edges if edge[1] != point]
        return quotient

    def check_sheaf_condition(self):
        if self._global_sections is None:
            self._global_sections = self.get_global_sections()
        for open_set in self.space:
            global_section = self._global_sections[open_set]
            for seed1 in global_section:
                for seed2 in global_section:
                    if seed1.germ != seed2.germ:
                        for connector1, germ1 in seed1.edges:
                            for connector2, germ2 in seed2.edges:
                                if germ1 == germ2:
                                    overlap = self.overlap([OpenSet([germ1]), OpenSet([connector1, connector2])])
                                    s1 = [s[germ1] for s in self.stalk(germ1) if set(s.values()) == set([connector1])]
                                    s2 = [s[germ1] for s in self.stalk(germ1) if set(s.values()) == set([connector2])]
                                    if overlap and set(s1) != set(s2):
                                        raise Exception("Sheaf condition not satisfied")

    def get_global_sections(self):
        global_sections = {}
        for open_set in self.space:
            sections = self.sections(open_set)
            global_section = set()
            for seed in sections:
                global_section.add(seed)
                for connector, germ in seed.edges:
                    if germ != seed.germ:
                        overlap = self.overlap([OpenSet([germ]), OpenSet([connector])])
                        if overlap:
                            if germ not in global_sections:
                                global_sections[germ] = set()
                            quotient = {}
                            for s in global_section:
                                if germ in s:
                                    quotient[s.germ] = [edge[1] for edge in s.edges if edge[1] != germ]
                            for s in global_section:
                                if germ not in s:
                                    quotient[s.germ] = [connector]
                            stalk = quotient
                            for s in global_section:
                                if germ in s:
                                    s.edges.append((connector, germ))
                            global_sections[germ].add(Seed(germ, [(edge[0], connector) for edge in seed.edges if edge[1] == germ])))
            global_sections[open_set] = global_section
        return global_sections

    def localize(self, tensor):
        localized_tensor = []
        for point in self.space:
            sections = self.stalk(point)
            localized_tensor.append(torch.stack([torch.Tensor(sections.get(germ, [])) for germ in tensor]))
        return torch.stack(localized_tensor)
