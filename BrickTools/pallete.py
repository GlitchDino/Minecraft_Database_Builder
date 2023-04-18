class Pallete:
    def __init__(self, input=None, distribution=None, customArr=False):
        self.input=input
        self.distribution=distribution
        self.customArr=customArr
        self.labeledPallete={}
        
        self.structureBlocks=[]
        self.functionBlocks=[]
        self.magicBlocks=[]
        self.trashBlocks=[]
        self.aestheticBlocks=[]


        #BLOCK ARRAY
        #Trash
        self.air=[
            "air",
            "void_air",
            "cave_air",
            "bubble_column"
        ]
        self.dirt=[
            "grass_block",
            "dirt",
            "coarse_dirt",
            "podzol",
            "farmland",
            "mycelium",
            "grass_path",
            "dirt_path",
            "rooted_dirt",
        ]
        self.sand=[
            "sand",
            "red_sand",
            "gravel",
            "clay",
            "terracotta",
        ]
        self.sappling=[
            "oak_sapling",
            "spruce_sapling",
            "birch_sapling",
            "jungle_sapling",
            "acacia_sapling",
            "dark_oak_sapling",
            "bamboo_sapling",
        ]
        self.infested=[
            "infested_stone",
            "infested_cobblestone",
            "infested_stone_bricks",
            "infested_mossy_stone_bricks",
            "infested_cracked_stone_bricks",
            "infested_chiseled_stone_bricks",
            "infested_deepslate"
        ]                 
        self.leaves=[
            "oak_leaves",
            "spruce_leaves",
            "birch_leaves",
            "jungle_leaves",
            "acacia_leaves",
            "dark_oak_leaves",
            "azalea_leaves",
            "flowering_azalea_leaves"
        ]
        self.grass=[
            "tall_seagrass",
            "grass",
            "fern",
            "large_fern",
            "dead_bush",
            "seagrass",
            "tall_grass",
        ]

        self.trashArray=[self.air, self.dirt, self.sand, self.sappling, self.infested, self.leaves, self.grass]
        
        #Structure
        self.woods=[
            "oak_log",
            "spruce_log",
            "birch_log",
            "jungle_log",
            "acacia_log",
            "dark_oak_log",
            "stripped_oak_log",
            "stripped_spruce_log",
            "stripped_birch_log",
            "stripped_spruce_log",
            "stripped_jungle_log",
            "stripped_acacia_log",
            "stripped_dark_oak_log",
            "stripped_oak_wood",
            "stripped_spruce_wood",
            "stripped_birch_wood",
            "stripped_jungle_wood",
            "stripped_acacia_wood",
            "stripped_dark_oak_wood",
            "oak_wood",
            "spruce_wood",
            "birch_wood",
            "jungle_wood",
            "acacia_wood",
            "dark_oak_wood",
        ]
        self.bricks=[
            "bricks",
            "stone_bricks",
            "mossy_stone_bricks",
            "cracked_stone_bricks",
            "chiseled_stone_bricks",
            "nether_bricks",
            "end_stone_bricks",
            "prismarine_bricks",
            "red_nether_bricks",
            "polished_blackstone_bricks",
            "cracked_polished_blackstone_bricks",
            "cracked_deepslate_bricks",
            "deepslate_bricks",
            "cracked_nether_bricks",
            "chiseled_nether_bricks"
            "quartz_bricks"
        ]
        self.nonNaturalStone=[
            "polished_granite",
            "polished_diorite",
            "polished_andesite",
            "cobblestone",
            "smooth_red_sandstone",
            "smooth_quartz",
            "chiseled_sandstone",
            "cut_sandstone",
            "smooth_sandstone",
            "smooth_stone",
            "mossy_cobblestone",
            "chiseled_red_sandstone",
            "cut_red_sandstone",
            "gilded_blackstone",
            "polished_blackstone",
            "cracked_deepslate_tiles",
            "deepslate_tiles",
            "chiseled_polished_blackstone",
            "chiseled_deepslate",
            "cobbled_deepslate",
            "quartz_block",
            "purpur_block",
            "purpur_pillar",
            "quartz_pillar",
            "smooth_basalt",
            "chiseled_quartz_block",
            "polished_deepslate",
            "prismarine",
            "dark_prismarine", 
            "crying_obsidian",
        ]
        self.planks=[
            "oak_planks",
            "spruce_planks",
            "birch_planks",
            "jungle_planks",
            "acacia_planks",
            "dark_oak_planks",
            "crimson_planks",
            "warped_planks",
        ]
        self.wool=[
            "white_wool",
            "orange_wool",
            "magenta_wool",
            "light_blue_wool",
            "yellow_wool",
            "lime_wool",
            "pink_wool",
            "gray_wool",
            "light_gray_wool",
            "cyan_wool",
            "purple_wool",
            "blue_wool",
            "brown_wool",
            "green_wool",
            "red_wool",
            "black_wool"
        ]
        self.overWorldSpecial=[
            "blackstone",
            "netherrack",
            "soul_soil",
            "soul_sand",
            "crimson_nylium",
            "warped_nylium",
            "crimson_stem",
            "warped_stem",
            "stripped_crimson_stem",
            "stripped_warped_stem",
            "stripped_crimson_hyphae",
            "stripped_warped_hyphae",
            "crimson_hyphae",
            "warped_hyphae",
            "warped_wart_block",
            "basalt",
            "polished_basalt",
            "ancient_debris",
            "end_stone",
            "nether_wart_block",
        ]
        self.nonNaturalOre=[
            "coal_block",
            "magma_block",
            "lapis_block",
            "gold_block",
            "iron_block",
            "emerald_block",
            "diamond_block",
            "cut_copper",
            "exposed_copper",
            "exposed_cut_copper",
            "oxidized_copper",
            "oxidized_cut_copper",
            "copper_block",
            "waxed_copper_block",
            "waxed_cut_copper",
            "waxed_exposed_copper",
            "waxed_exposed_cut_copper",
            "waxed_oxidized_copper",
            "waxed_oxidized_cut_copper",
            "waxed_weathered_copper"
            "waxed_weathered_cut_copper",
            "weathered_copper",
            "weathered_cut_copper"
            "amethyst_block",
            "netherite_block",
            "iron_bars",
            "chain",
        ]
        self.glass=[
            "glass",
            "white_stained_glass",
            "orange_stained_glass",
            "magenta_stained_glass",
            "light_blue_stained_glass",
            "yellow_stained_glass",
            "lime_stained_glass",
            "pink_stained_glass",
            "gray_stained_glass",
            "light_gray_stained_glass",
            "cyan_stained_glass",
            "purple_stained_glass",
            "blue_stained_glass",
            "brown_stained_glass",
            "green_stained_glass",
            "red_stained_glass",
            "tinted_glass",
        ]
        self.glass_panes=[
            "glass_pane",
            "black_stained_glass",
            "white_stained_glass_pane",
            "orange_stained_glass_pane",
            "magenta_stained_glass_pane",
            "light_blue_stained_glass_pane",
            "yellow_stained_glass_pane",
            "lime_stained_glass_pane",
            "pink_stained_glass_pane",
            "gray_stained_glass_pane",
            "light_gray_stained_glass_pane",
            "cyan_stained_glass_pane",
            "purple_stained_glass_pane",
            "blue_stained_glass_pane",
            "brown_stained_glass_pane",
            "green_stained_glass_pane",
            "red_stained_glass_pane",
            "black_stained_glass_pane",
        ]
        self.slabs=[
            "oak_slab",
            "spruce_slab",
            "birch_slab",
            "jungle_slab",
            "acacia_slab",
            "dark_oak_slab",
            "stone_slab",
            "sandstone_slab",
            "petrified_oak_slab",
            "cobblestone_slab",
            "brick_slab",
            "stone_brick_slab",
            "nether_brick_slab",
            "quartz_slab",
            "red_sandstone_slab",
            "purpur_slab",
            "prismarine_slab",
            "prismarine_brick_slab",
            "dark_prismarine_slab",
            "smooth_stone_slab",
            "cut_sandstone_slab",
            "cut_red_sandstone_slab",
            "polished_granite_slab",
            "smooth_red_sandstone_slab",
            "mossy_stone_brick_slab",
            "polished_diorite_slab",
            "mossy_cobblestone_slab",
            "end_stone_brick_slab",
            "smooth_sandstone_slab",
            "smooth_quartz_slab",
            "granite_slab",
            "andesite_slab",
            "red_nether_brick_slab",
            "polished_andesite_slab",
            "diorite_slab",
            "crimson_slab",
            "warped_slab",
            "blackstone_slab",
            "polished_blackstone_slab",
            "polished_blackstone_brick_slab",
            "cobbled_deepslate_slab",
            "cut_copper_slab",
            "deepslate_brick_slab",
            "deepslate_tile_slab",
            "exposed_cut_copper_slab",
            "oxidized_cut_copper_slab",
            "polished_deepslate_slab",
            "waxed_cut_copper_slab",
            "waxed_exposed_cut_copper_slab",
            "waxed_oxidized_cut_copper_slab",
            "waxed_weathered_cut_copper_slab",
            "weathered_cut_copper_slab",
        ]
        self.walls=[
            "cobblestone_wall",
            "mossy_cobblestone_wall",
            "nether_brick_fence",
            "brick_wall",
            "prismarine_wall",
            "red_sandstone_wall",
            "mossy_stone_brick_wall",
            "granite_wall",
            "stone_brick_wall",
            "nether_brick_wall",
            "andesite_wall",
            "red_nether_brick_wall",
            "sandstone_wall",
            "end_stone_brick_wall",
            "diorite_wall",
            "blackstone_wall",
            "polished_blackstone_wall",
            "polished_blackstone_brick_wall",
            "cobbled_deepslate_wall",
            "deepslate_brick_wall",
            "deepslate_tile_wall",
            "polished_deepslate_wall"
        ]
        self.fence_gate=[
            "dark_oak_fence_gate",
            "oak_fence_gate",
            "spruce_fence_gate",
            "birch_fence_gate",
            "jungle_fence_gate",
            "acacia_fence_gate",
            "dark_oak_fence_gate",
            "crimson_fence_gate",
            "warped_fence_gate"
        ]
        self.fence=[
            "oak_fence",
            "spruce_fence",
            "birch_fence",
            "jungle_fence",
            "acacia_fence",
            "dark_oak_fence",
            "crimson_fence",
            "warped_fence",
        ]
        self.stairs=[
            "purpur_stairs",
            "oak_stairs",
            "cobblestone_stairs",
            "brick_stairs",
            "stone_brick_stairs",
            "nether_brick_stairs",
            "sandstone_stairs",
            "spruce_stairs",
            "birch_stairs",
            "jungle_stairs",
            "quartz_stairs",
            "acacia_stairs",
            "dark_oak_stairs",
            "prismarine_stairs",
            "prismarine_brick_stairs",
            "dark_prismarine_stairs",
            "red_sandstone_stairs",
            "polished_granite_stairs",
            "smooth_red_sandstone_stairs",
            "mossy_stone_brick_stairs",
            "polished_diorite_stairs",
            "mossy_cobblestone_stairs",
            "end_stone_brick_stairs",
            "stone_stairs",
            "smooth_sandstone_stairs",
            "smooth_quartz_stairs",
            "granite_stairs",
            "andesite_stairs",
            "red_nether_brick_stairs",
            "polished_andesite_stairs",
            "polished_andesite_stairs",
            "diorite_stairs",
            "crimson_stairs",
            "warped_stairs",
            "blackstone_stairs",
            "polished_blackstone_stairs",
            "polished_blackstone_brick_stairs",
            "cobbled_deepslate_stairs",
            "cut_copper_stairs",
            "deepslate_brick_stairs",
            "deepslate_tile_stairs",
            "exposed_cut_copper_stairs",
            "oxidized_cut_copper_stairs",
            "polished_deepslate_stairs",
            "waxed_cut_copper_stairs",
            "waxed_exposed_cut_copper_stairs",
            "waxed_oxidized_cut_copper_stairs",
            "waxed_weathered_cut_copper_stairs",
            "weathered_cut_copper_stairs"
        ]
        self.teracotta=[
            "white_terracotta",
            "orange_terracotta",
            "magenta_terracotta",
            "light_blue_terracotta",
            "yellow_terracotta",
            "lime_terracotta",
            "pink_terracotta",
            "gray_terracotta",
            "light_gray_terracotta",
            "cyan_terracotta",
            "purple_terracotta",
            "blue_terracotta",
            "brown_terracotta",
            "green_terracotta",
            "red_terracotta",
            "black_terracotta",
        ]
        self.glazed_teracotta=[
            "white_glazed_terracotta",
            "orange_glazed_terracotta",
            "magenta_glazed_terracotta",
            "light_blue_glazed_terracotta",
            "yellow_glazed_terracotta",
            "lime_glazed_terracotta",
            "pink_glazed_terracotta",
            "gray_glazed_terracotta",
            "light_gray_glazed_terracotta",
            "cyan_glazed_terracotta",
            "purple_glazed_terracotta",
            "blue_glazed_terracotta",
            "brown_glazed_terracotta",
            "green_glazed_terracotta",
            "red_glazed_terracotta",
            "black_glazed_terracotta"
        ]
        self.concrete=[
            "white_concrete",
            "orange_concrete",
            "magenta_concrete",
            "light_blue_concrete",
            "yellow_concrete",
            "lime_concrete",
            "pink_concrete",
            "gray_concrete",
            "light_gray_concrete",
            "cyan_concrete",
            "purple_concrete",
            "blue_concrete",
            "brown_concrete",
            "green_concrete",
            "red_concrete",
            "black_concrete"
        ]
        self.concrete_powder=[
            "white_concrete_powder",
            "orange_concrete_powder",
            "magenta_concrete_powder",
            "light_blue_concrete_powder",
            "yellow_concrete_powder",
            "lime_concrete_powder",
            "pink_concrete_powder",
            "gray_concrete_powder",
            "light_gray_concrete_powder",
            "cyan_concrete_powder",
            "purple_concrete_powder",
            "blue_concrete_powder",
            "brown_concrete_powder",
            "green_concrete_powder",
            "red_concrete_powder",
            "black_concrete_powder"
        ]

        self.structureArray=[self.woods,self.bricks,self.nonNaturalStone, self.planks, self.wool, self.overWorldSpecial,self.nonNaturalOre, self.glass, self.glass_panes, self.slabs, self.walls, self.fence_gate, self.fence, self.stairs,self.teracotta, self.glazed_teracotta, self.concrete, self.concrete_powder]
        #Aesthetic 
        self.decorativeBlocks=[
            "painting",
            "cobweb",
            "bookshelf",
            "carved_pumpkin",
            "jack_o_lantern",
            "vine",
            "weeping_vines",
            "twisting_vines",
            "hay_block",
            "slime_block",
            "dragon_egg",
            "turtle_egg",
            "egg",
            "honey_block",
            "honeycomb_block",
            "item_frame",
            "cake",
            "bone_block", 
            "shulker_shell",
            "glow_item_frame",
            "bee_nest",
            "beehive",
        ]
        self.decortiveUseBlocks=[
            "armor_stand",
            "tnt",
            "lectern",
            "bell",
            "campfire",
            "soul_campfire",
            "target",
            "lightning_rod",
            "end_portal_frame",
        ]
        self.banner=[
            "white_banner",
            "orange_banner",
            "magenta_banner",
            "light_blue_banner",
            "yellow_banner",
            "lime_banner",
            "pink_banner",
            "gray_banner",
            "light_gray_banner",
            "cyan_banner",
            "purple_banner",
            "blue_banner",
            "brown_banner",
            "green_banner",
            "red_banner",
            "black_banner"
        ]
        self.wall_banner=[
            "white_wall_banner",
            "orange_wall_banner",
            "magenta_wall_banner",
            "light_blue_wall_banner",
            "yellow_wall_banner",
            "lime_wall_banner",
            "pink_wall_banner",
            "gray_wall_banner",
            "light_gray_wall_banner",
            "cyan_wall_banner",
            "purple_wall_banner",
            "blue_wall_banner",
            "brown_wall_banner",
            "green_wall_banner",
            "red_wall_banner",
            "black_wall_banner",
        ]
        self.trapdoor=[
            "oak_trapdoor",
            "spruce_trapdoor",
            "birch_trapdoor",
            "jungle_trapdoor",
            "acacia_trapdoor",
            "dark_oak_trapdoor",
            "iron_trapdoor",
            "crimson_trapdoor",
            "warped_trapdoor"
        ]
        self.carpet=[
            "white_carpet",
            "orange_carpet",
            "magenta_carpet",
            "light_blue_carpet",
            "yellow_carpet",
            "lime_carpet",
            "pink_carpet",
            "gray_carpet",
            "light_gray_carpet",
            "cyan_carpet",
            "purple_carpet",
            "blue_carpet",
            "brown_carpet",
            "green_carpet",
            "red_carpet",
            "black_carpet",
            "moss_carpet"
        ]
        self.candle=[
            "black_candle",
            "blue_candle",
            "brown_candle",
            "candle",
            "cyan_candle",
            "gray_candle",
            "green_candle",
            "light_blue_candle",
            "light_gray_candle",
            "lime_candle",
            "magenta_candle",
            "orange_candle",
            "pink_candle",
            "purple_candle",
            "red_candle",
            "white_candle",
            "yellow_candle"
        ]
        self.pot=[
            "flower_pot",
            "potted_oak_sapling",
            "potted_spruce_sapling",
            "potted_birch_sapling",
            "potted_jungle_sapling",
            "potted_acacia_sapling",
            "potted_dark_oak_sapling",
            "potted_fern",
            "potted_dandelion",
            "potted_poppy",
            "potted_blue_orchid",
            "potted_allium",
            "potted_azure_bluet",
            "potted_red_tulip",
            "potted_orange_tulip",
            "potted_white_tulip",
            "potted_pink_tulip",
            "potted_oxeye_daisy",
            "potted_red_mushroom",
            "potted_brown_mushroom",
            "potted_dead_bush",
            "potted_cactus",
            "potted_cornflower",
            "potted_lily_of_the_valley",
            "potted_wither_rose",
            "potted_bamboo",
            "potted_crimson_fungus",
            "potted_warped_fungus",
            "potted_crimson_roots",
            "potted_warped_roots",
            "hanging_roots"
        ]
        self.skulls=[
            "skeleton_skull",
            "wither_skeleton_skull",
            "player_head",
            "zombie_head",
            "creeper_head",
            "dragon_head",
            "skeleton_wall_skull",
            "wither_skeleton_wall_skull",
            "zombie_wall_head",
            "player_wall_head",
            "creeper_wall_head",
            "dragon_wall_head",
        ]

        self.aestheticArray=[self.decorativeBlocks, self.decortiveUseBlocks, self.banner, self.wall_banner,self.trapdoor,self.carpet,self.candle,self.pot,self.skulls]
        
        #Function
        self.lights=[
            "wall_torch",
            "redstone_wall_torch",
            "torch",
            "soul_torch",
            "soul_wall_torch",
            "redstone_torch",
            "glowstone",
            "end_rod",
            "redstone_lamp",
            "lantern",
            "sea_lantern",
            "soul_lantern",
            "shroomlight",
            "glow_lichen",
        ]
        self.button=[
            "oak_button",
            "spruce_button",
            "birch_button",
            "jungle_button",
            "acacia_button",
            "dark_oak_button",
            "crimson_button",
            "warped_button",
            "polished_blackstone_button",
            "stone_button",
        ]
        self.useBlocks=[
            "crafting_table",
            "furnace",
            "ladder",
            "enchanting_table",
            "beacon",
            "anvil",
            "chipped_anvil",
            "damaged_anvil",
            "brewing_stand",
            "cauldron",
            "barrel",
            "smoker",
            "blast_furnace",
            "cartography_table",
            "fletching_table",
            "grindstone",
            "composter",
            "loom",
            "smithing_table",
            "stonecutter",
            "lodestone",
            "scaffolding", 
        ]
        self.chest=[
            "chest",
            "ender_chest",
            "trapped_chest",
        ]
        self.shulker_box=[
            "shulker_box",
            "white_shulker_box",
            "orange_shulker_box",
            "magenta_shulker_box",
            "light_blue_shulker_box",
            "yellow_shulker_box",
            "lime_shulker_box",
            "pink_shulker_box",
            "gray_shulker_box",
            "light_gray_shulker_box",
            "cyan_shulker_box",
            "purple_shulker_box",
            "blue_shulker_box",
            "brown_shulker_box",
            "green_shulker_box",
            "red_shulker_box",
            "black_shulker_box"
        ]
        self.pressure_plate=[
            "stone_pressure_plate",
            "oak_pressure_plate",
            "spruce_pressure_plate",
            "birch_pressure_plate",
            "jungle_pressure_plate",
            "acacia_pressure_plate",
            "dark_oak_pressure_plate",
            "light_weighted_pressure_plate",
            "heavy_weighted_pressure_plate",
            "crimson_pressure_plate",
            "warped_pressure_plate",
            "polished_blackstone_pressure_plate"
        ]
        self.minecart=[
            "minecart",
            "chest_minecart",
            "furnace_minecart",
            "tnt_minecart",
            "hopper_minecart",
            "command_block_minecart"]
        self.doors=[
            "iron_door",
            "oak_door",
            "spruce_door",
            "birch_door",
            "jungle_door",
            "acacia_door",
            "dark_oak_door",
            "crimson_door",
            "warped_door",
        ]
        self.signs=[
            "sign",
            "wall_sign",
            "oak_sign",
            "spruce_sign",
            "birch_sign",
            "jungle_sign",
            "acacia_sign",
            "dark_oak_sign",
            "crimson_sign",
            "warped_sign",
            "oak_wall_sign",
            "spruce_wall_sign",
            "birch_wall_sign",
            "acacia_wall_sign",
            "jungle_wall_sign",
            "dark_oak_wall_sign",
            "crimson_wall_sign",
            "warped_wall_sign"

        ]
        self.bed=[
            "white_bed",
            "orange_bed",
            "magenta_bed",
            "light_blue_bed",
            "yellow_bed",
            "lime_bed",
            "pink_bed",
            "gray_bed",
            "light_gray_bed",
            "cyan_bed",
            "purple_bed",
            "blue_bed",
            "brown_bed",
            "green_bed",
            "red_bed",
            "black_bed",
        ]

        self.functionArray=[self.lights, self.button, self.useBlocks, self.chest, self.shulker_box, self.pressure_plate, self.minecart, self.doors, self.signs, self.bed]
        #magic
        self.naturalStone=[
            "granite",
            "stone",
            "diorite",
            "sandstone",
            "andesite",
            "bedrock",
            "obsidian",
            "crying_obsidian",
            "red_sandstone",
            "calcite",
            "deepslate",
            "dripstone_block",
            "pointed_dripstone",
            "tuff"
        ]
        self.ore=[
            "gold_ore",
            "iron_ore",
            "coal_ore",
            "lapis_ore",
            "emerald_ore",
            "redstone_ore",
            "diamond_ore",
            "nether_quartz_ore",
            "nether_gold_ore",
            "copper_ore",
            "deepslate_coal_ore",
            "deepslate_copper_ore",
            "deepslate_diamond_ore",
            "deepslate_emerald_ore",
            "deepslate_gold_ore",
            "deepslate_iron_ore",
            "deepslate_lapis_ore",
            "deepslate_redstone_ore",
            "raw_copper_block",
            "raw_gold_block",
            "raw_iron_block",

        ]
        self.plant_block=[
            "dried_kelp_block",
            "cactus",
            "sponge",
            "wet_sponge",
            "brown_mushroom_block",
            "red_mushroom_block",
            "mushroom_stem",
            "pumpkin",
            "melon",
        ]
        self.plant=[
            "kelp_plant",
            "lily_pad",
            "bamboo",
            "sweet_berry_bush",
            "sugar_cane",
            "kelp",
            "big_dripleaf",
            "small_dripleaf",
            "weeping_vines_plant",
            "twisting_vines_plant",
            "budding_amethyst",
            "large_amethyst_bud",
            "medium_amethyst_bud",
            "small_amethyst_bud",
            "sea_pickle",   
            "azalea",
            "budding_amethyst",
            "brown_mushroom",
            "red_mushroom",  
            "flowering_azalea",     
        ]
        self.spawner=[
            "spawner"
            ]
        self.items=[
            "bundle",
            "bundle_filled",
            "turtle_helmet",
            "scute",
            "iron_shovel",
            "iron_pickaxe",
            "iron_axe",
            "flint_and_steel",
            "apple",
            "bow",
            "arrow",
            "coal",
            "charcoal",
            "diamond",
            "iron_ingot",
            "gold_ingot",
            "iron_sword",
            "wooden_sword",
            "spyglass",
            "filled_map",
            "shield",
            "elytra",
            "clock",
            "writable_book",
        ]
        self.flower=[
            "dandelion",
            "poppy",
            "blue_orchid",
            "allium",
            "azure_bluet",
            "red_tulip",
            "orange_tulip",
            "white_tulip",
            "pink_tulip",
            "chorus_plant",
            "chorus_flower",
            "cornflower",
            "lily_of_the_valley",
            "wither_rose",
            "crimson_fungus",
            "warped_fungus",
            "crimson_roots",
            "warped_roots",
            "nether_sprouts",
            "sunflower",
            "lilac",
            "rose_bush",
            "peony",
            "oxeye_daisy",
            "wheat",
            "carrots",
            "potatoes",
            "beetroots",
        ]
        self.states=[
            "nether_portal",
            "end_portal",
            "soul_fire",
            "fire",
            "barrier",
            "structure_void",
            "end_gateway",
        ]
        self.coral_block=[
            "tube_coral_block",
            "brain_coral_block",
            "bubble_coral_block",
            "fire_coral_block",
            "horn_coral_block"
        ]
        self.dead_coral_block=[
            "dead_tube_coral_block",
            "dead_brain_coral_block",
            "dead_bubble_coral_block",
            "dead_fire_coral_block",
            "dead_horn_coral_block",
        ]
        self.coral=[
            "tube_coral",
            "brain_coral",
            "bubble_coral",
            "fire_coral",
            "horn_coral",
        ]
        self.dead_coral=[
            "dead_tube_coral",
            "dead_brain_coral",
            "dead_bubble_coral",
            "dead_fire_coral",
            "dead_horn_coral"
        ]
        self.coral_fan=[
            "tube_coral_fan",
            "brain_coral_fan",
            "bubble_coral_fan",
            "fire_coral_fan",
            "horn_coral_fan"
        ]
        self.dead_coral_fan=[
            "dead_tube_coral_fan",
            "dead_brain_coral_fan",
            "dead_bubble_coral_fan",
            "dead_fire_coral_fan",
            "dead_horn_coral_fan"
        ]
        self.dead_coral_wall_fan=[
            "dead_tube_coral_wall_fan",
            "dead_brain_coral_wall_fan",
            "dead_bubble_coral_wall_fan",
            "dead_fire_coral_wall_fan",
            "dead_horn_coral_wall_fan"
        ]
        self.coral_wall_fan=[
            "tube_coral_wall_fan",
            "brain_coral_wall_fan",
            "bubble_coral_wall_fan",
            "fire_coral_wall_fan",
            "horn_coral_wall_fan"
        ]
        self.redStone=[
            "dispenser",
            "note_block",
            "powered_rail",
            "detector_rail",
            "sticky_piston",
            "piston",
            "spawner",
            "rail",
            "lever",
            "jukebox",
            "command_block",
            "daylight_detector",
            "redstone_block",
            "hopper",
            "activator_rail",
            "dropper",
            "repeating_command_block",
            "chain_command_block",
            "observer",
            "conduit",
            "repeater",
            "comparator",
            "structure_block",
            "redstone",
            "piston_head",
            "moving_piston",
            "redstone_wire",
            "jigsaw",
            "respawn_anchor",
            "moss_block",
            "sculk_sensor"
            "lever",
            "tripwire_hook",
        ]
        self.ice=[
            "snow",
            "snow_block",
            "ice",
            "packed_ice",
            "blue_ice",
            "frosted_ice",
        ]
        self.fluids=[
            "water",
            "lava"
        ]
        
        self.magicArray=[self.naturalStone, self.ore, self.plant, self.plant_block,self.spawner,self.items, self.flower, self.states, self.coral_block, self.dead_coral_block, self.coral, self.dead_coral, self.coral_fan, self.dead_coral_fan, self.dead_coral_wall_fan, self.coral_wall_fan, self.redStone, self.ice, self.fluids]

        #"crying_obsidian",
        self.netherNatural=[
            "blackstone",
            "netherrack",
            "soul_soil",
            "soul_sand",
            "crimson_nylium",
            "warped_nylium",
            "crimson_stem",
            "warped_stem",
            "stripped_crimson_stem",
            "stripped_warped_stem",
            "stripped_crimson_hyphae",
            "stripped_warped_hyphae",
            "crimson_hyphae",
            "warped_hyphae",
            "warped_wart_block",
            "basalt",
            "polished_basalt",
            "ancient_debris",
            "end_stone",
            "nether_wart_block",
        ]
        
    def buildPallete(self):
        #stopped at page 8
       
        #https://minecraftitemids.com/8
        if(self.customArr==False):
            for item in self.trashArray:
                self.trashBlocks.extend(item)
            
            for item in self.magicArray:
                self.magicBlocks.extend(item)

            for item in self.functionArray:
                self.functionBlocks.extend(item)

            for item in self.structureArray:
                self.structureBlocks.extend(item)

            for item in self.aestheticArray:
                self.aestheticBlocks.extend(item)

            for block in self.distribution:
                if(block in self.trashBlocks):
                    self.labeledPallete[block]="trash"
                elif(block in self.functionBlocks):
                    self.labeledPallete[block]="function"
                elif(block in self.aestheticBlocks):
                    self.labeledPallete[block]="aesthetic"
                elif(block in self.structureBlocks):
                    self.labeledPallete[block]="structure"
                elif(block in self.magicArray):
                    print("INPUT NEEDED\n a=aesthetic, f=function, s=structure, t=trash\n>")
                    x=False
                    while(x==False):
                        res=input()
                        if(res=="a"):
                            self.labeledPallete[block]="aesthetic"
                            x=True
                        elif(res=="f"):
                            self.labeledPallete[block]="function"
                            x=True
                        elif(res=="s"):
                            self.labeledPallete[block]="structure"
                            x=True
                        elif(res=="t"):
                            self.labeledPallete[block]="trash"
                            x=True 
                        else:
                            print("Invalid input")
                else:
                    print(block)
                    #EDIT THIS PLEASE 
                    #basically says all magic blocks are aesthetic
                    self.labeledPallete[block]="aesthetic"
                    print("BLOCK NOT FOUND")
            
            return self.labeledPallete

    def get_trash(self):
        trash=[]
        trash.extend(self.air)
        trash.extend(self.dirt)
        trash.extend(self.sand)
        trash.extend(self.sappling)
        trash.extend(self.infested)
        trash.extend(self.grass)

        return trash
    
    def get_all_magic(self):
        all_magic=[]
        for item in self.magicArray:
            all_magic.extend(item)
        return all_magic
    
    def get_all_trash(self):
        all_trash=[]
        for item in self.trashArray:
            all_trash.extend(item)
        return all_trash
    
    def get_all_function(self):
        all_func=[]
        for item in self.functionArray:
            all_func.extend(item)
        return all_func
    def get_all_structure(self):
        all_struct=[]
        for item in self.structureArray:
            all_struct.extend(item)
        return all_struct
    
    def get_all_aesthetic(self):
        all_aesth=[]
        for item in self.aestheticArray:
            all_aesth.extend(item)
        return all_aesth       
    
    def get_all_ids(self):
        for item in self.trashArray:
            self.trashBlocks.extend(item)
        
        for item in self.magicArray:
            self.magicBlocks.extend(item)

        for item in self.functionArray:
            self.functionBlocks.extend(item)

        for item in self.structureArray:
            self.structureBlocks.extend(item)

        for item in self.aestheticArray:
            self.aestheticBlocks.extend(item)
        all=[]
        all.extend(self.trashBlocks)
        all.extend(self.magicBlocks)
        all.extend(self.functionBlocks)
        all.extend(self.structureBlocks)
        all.extend(self.aestheticBlocks)
        return all


#t=['air', 'oak_planks', 'cobblestone', 'stone_bricks', 'oak_door', 'furnace', 'red_wool', 'red_bed', 'chest', 'spruce_log', 'oak_trapdoor', 'spruce_planks', 'anvil', 'ladder', 'wall_torch', 'glass_pane', 'potted_poppy', 'light_gray_candle', 'spruce_stairs']
#p=Pallete("haha", t)
#z=p.buildPallete()