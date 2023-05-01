from collections import defaultdict

def overlap(open_sets):
    return set.intersection(*open_sets)

def local(open_set, graph):
    return {Seed(v, [(v, w) for w in graph[v] if w in open_set]) for v in open_set if v in graph}

class SemanticSheaf:
    def __init__(self, space, overlap_func, local_func):
        self.space = space
        self.overlap_func = overlap_func
        self.local_func = local_func
        self._global_sections = None
        self.sheaves = {}
        self.cluster_dict = defaultdict(set)

    def build_clusters(self, clusters):
        for i, c in enumerate(clusters):
            for germ in c:
                self.cluster_dict[germ].add(i)

    def build_sheaves(self):
        for c, i in self.cluster_dict.items():
            sheaf = SheafTopology(self.space, self.overlap_func, self.local_func)
            sheaf.check_sheaf_condition = lambda: None
            sheaf.get_global_sections = lambda: self._global_sections[i]
            self.sheaves[c] = sheaf

    def get_global_sections(self):
        global_sections = {}
        for i, sheaf in self.sheaves.items():
            sheaf._global_sections = sheaf.get_global_sections()
            for open_set, global_section in sheaf._global_sections.items():
                if open_set not in global_sections:
                    global_sections[open_set] = set()
                for seed in global_section:
                    new_seed = Seed(seed.germ, [(edge[0], c) for edge in seed.edges if edge[1] in self.cluster_dict])
                    global_sections[open_set].add(new_seed)
        return global_sections

    def gluing_maps(self, clusters):
        gluing_maps = {}
        for i, c in enumerate(clusters):
            gluing_maps[i] = {}
            for germ in c:
                gluing_maps[i][germ] = self.cluster_dict[germ]
        return gluing_maps

