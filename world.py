import random

class WorldGeneration:
    def __init__(self):
        self.geographical_features = self.generate_geographical_features()
        self.biomes = self.generate_biomes()
        self.rivers = self.generate_rivers()
        self.mountains = self.generate_mountains()
        self.forests = self.generate_forests()
        self.deserts = self.generate_deserts()
        self.oceans = self.generate_oceans()

    def generate_geographical_features(self):
        feature_types = ["Mountain Range", "Valley", "River", "Forest", "Desert", "Ocean"]
        geographical_features = [GeographicalFeature(random.choice(feature_types), self.generate_description()) for _ in range(100)]
        return geographical_features

    def generate_biomes(self):
        biome_types = ["Tropical Rainforest", "Savanna", "Desert", "Grassland", "Deciduous Forest", "Taiga", "Tundra", "Alpine"]
        biomes = [Biome(random.choice(biome_types), self.generate_description()) for _ in range(100)]
        return biomes

    def generate_rivers(self):
        river_names = ["Amazon", "Nile", "Yangtze", "Mississippi", "Yellow", "Ganges", "Danube", "Volga"]
        rivers = [River(random.choice(river_names), self.generate_description()) for _ in range(50)]
        return rivers

    def generate_mountains(self):
        mountain_names = ["Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu", "Cho Oyu", "Dhaulagiri", "Manaslu"]
        mountains = [Mountain(random.choice(mountain_names), self.generate_description()) for _ in range(50)]
        return mountains

    def generate_forests(self):
        forest_names = ["Amazon", "Congo", "Boreal", "Valdivian", "Daintree", "Sundarbans", "Black Forest", "Sherwood"]
        forests = [Forest(random.choice(forest_names), self.generate_description()) for _ in range(50)]
        return forests

    def generate_deserts(self):
        desert_names = ["Sahara", "Arabian", "Gobi", "Kalahari", "Sonoran", "Atacama", "Great Victoria", "Mojave"]
        deserts = [Desert(random.choice(desert_names), self.generate_description()) for _ in range(50)]
        return deserts

    def generate_oceans(self):
        ocean_names = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
        oceans = [Ocean(random.choice(ocean_names), self.generate_description()) for _ in range(5)]
        return oceans

    def generate_description(self):
        descriptions = [
            "a vast and expansive area",
            "rich with diverse flora and fauna",
            "a place of extreme weather conditions",
            "home to many unique species",
            "a place of natural beauty and wonder",
            "a region with rich mineral resources",
            "a fertile land with abundant water sources",
            "a harsh and unforgiving terrain",
            "a place of mystical and magical occurrences",
            "a land of ancient ruins and lost civilizations"
        ]
        return random.choice(descriptions)


class GeographicalFeature:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.resources = self.generate_resources()

    def generate_resources(self):
        resources = ["Gold", "Silver", "Iron", "Coal", "Copper", "Diamonds", "Emeralds", "Sapphires", "Rubies", "Quartz"]
        return [random.choice(resources) for _ in range(random.randint(1, 5))]


class Biome:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.flora = self.generate_flora()
        self.fauna = self.generate_fauna()

    def generate_flora(self):
        flora_list = [
            "Oak Tree", "Pine Tree", "Cactus", "Fern", "Moss", "Bamboo", "Sagebrush", "Palm Tree", "Maple Tree", "Birch Tree",
            "Redwood Tree", "Sequoia Tree", "Mangrove Tree", "Eucalyptus Tree", "Baobab Tree", "Banyan Tree", "Willow Tree", "Cedar Tree",
            "Spruce Tree", "Fir Tree"
        ]
        return [random.choice(flora_list) for _ in range(random.randint(5, 15))]

    def generate_fauna(self):
        fauna_list = [
            "Deer", "Wolf", "Eagle", "Bear", "Fox", "Rabbit", "Snake", "Falcon", "Lynx", "Elk",
            "Moose", "Beaver", "Otter", "Badger","Moose", "Beaver", "Otter", "Badger", "Bison", "Cougar", "Panther", "Leopard", "Giraffe", "Elephant",
            "Rhino", "Hippopotamus", "Zebra", "Antelope", "Buffalo", "Gazelle", "Cheetah", "Hyena", "Kangaroo", "Koala",
            "Crocodile", "Alligator", "Komodo Dragon", "Iguana", "Chameleon", "Tortoise", "Sea Turtle", "Dolphin", "Whale",
            "Shark", "Octopus", "Jellyfish", "Starfish", "Seahorse", "Crab", "Lobster", "Shrimp", "Coral", "Seaweed"
        ]
        return [random.choice(fauna_list) for _ in range(random.randint(5, 15))]


class River:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.length = random.randint(100, 7000)  # Length in kilometers
        self.fish_species = self.generate_fish_species()

    def generate_fish_species(self):
        fish_species = [
            "Salmon", "Trout", "Catfish", "Carp", "Bass", "Pike", "Sturgeon", "Tilapia", "Perch", "Haddock",
            "Cod", "Mackerel", "Tuna", "Sardine", "Anchovy", "Herring", "Mahi Mahi", "Marlin", "Swordfish", "Shark"
        ]
        return [random.choice(fish_species) for _ in range(random.randint(3, 10))]


class Mountain:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.height = random.randint(1000, 8848)  # Height in meters
        self.mineral_resources = self.generate_mineral_resources()

    def generate_mineral_resources(self):
        mineral_resources = [
            "Gold", "Silver", "Iron", "Coal", "Copper", "Diamonds", "Emeralds", "Sapphires", "Rubies", "Quartz",
            "Granite", "Marble", "Limestone", "Slate", "Gypsum", "Salt", "Phosphate", "Zinc", "Nickel", "Uranium"
        ]
        return [random.choice(mineral_resources) for _ in range(random.randint(3, 10))]


class Forest:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.tree_species = self.generate_tree_species()
        self.wildlife = self.generate_wildlife()

    def generate_tree_species(self):
        tree_species = [
            "Oak", "Pine", "Cedar", "Birch", "Maple", "Redwood", "Sequoia", "Banyan", "Baobab", "Cherry",
            "Eucalyptus", "Fir", "Spruce", "Hemlock", "Cypress", "Palm", "Mangrove", "Bamboo", "Willow", "Teak"
        ]
        return [random.choice(tree_species) for _ in range(random.randint(5, 15))]

    def generate_wildlife(self):
        wildlife = [
            "Deer", "Rabbit", "Fox", "Bear", "Wolf", "Birds", "Squirrels", "Raccoons", "Opossums", "Skunks",
            "Porcupines", "Moose", "Elk", "Beaver", "Lynx", "Bobcat", "Coyote", "Wild Boar", "Bison", "Panther"
        ]
        return [random.choice(wildlife) for _ in range(random.randint(5, 15))]


class Desert:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.sand_dunes = random.randint(20, 500)  # Number of sand dunes
        self.oases = self.generate_oases()

    def generate_oases(self):
        oases = [
            "Palm Oasis", "Rock Oasis", "Lake Oasis", "River Oasis", "Spring Oasis", "Waterfall Oasis", "Cave Oasis", "Mountain Oasis"
        ]
        return [random.choice(oases) for _ in range(random.randint(1, 5))]


class Ocean:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.depth = random.randint(200, 11000)  # Depth in meters
        self.marine_life = self.generate_marine_life()

    def generate_marine_life(self):
        marine_life = [
            "Coral Reefs", "Fish Schools", "Shark Packs", "Dolphin Pods", "Whale Groups", "Seagrass Beds", "Kelp Forests", "Seashell Beds",
            "Crab Colonies", "Lobster Dens", "Jellyfish Swarms", "Seahorse Communities", "Octopus Gardens", "Sea Turtle Nesting Areas", "Seabird Colonies"
        ]
        return [random.choice(marine_life) for _ in range(random.randint(3, 10))]


# Instantiate the WorldGeneration class to generate a world
world_gen = WorldGeneration()
class GeographicalFeature:
    def __init__(self, name, description, resources):
        self.name = name
        self.description = description
        self.resources = resources

class Biome:
    def __init__(self, name, description, flora, fauna):
        self.name = name
        self.description = description
        self.flora = flora
        self.fauna = fauna

class River:
    def __init__(self, name, description, length, fish_species):
        self.name = name
        self.description = description
        self.length = length
        self.fish_species = fish_species

class Mountain:
    def __init__(self, name, description, height, mineral_resources):
        self.name = name
        self.description = description
        self.height = height
        self.mineral_resources = mineral_resources

class Forest:
    def __init__(self, name, description, tree_species, wildlife):
        self.name = name
        self.description = description
        self.tree_species = tree_species
        self.wildlife = wildlife

class Desert:
    def __init__(self, name, description, sand_dunes, oases):
        self.name = name
        self.description = description
        self.sand_dunes = sand_dunes
        self.oases = oases

class Ocean:
    def __init__(self, name, description, depth, marine_life):
        self.name = name
        self.description = description
        self.depth = depth
        self.marine_life = marine_life

class WorldGeneration:
    def __init__(self):
        self.geographical_features = [GeographicalFeature("Feature1", "Description1", ["Resource1", "Resource2"])]
        self.biomes = [Biome("Biome1", "Description1", ["Flora1", "Flora2"], ["Fauna1", "Fauna2"])]
        self.rivers = [River("River1", "Description1", 100, ["Fish1", "Fish2"])]
        self.mountains = [Mountain("Mountain1", "Description1", 2000, ["Mineral1", "Mineral2"])]
        self.forests = [Forest("Forest1", "Description1", ["Tree1", "Tree2"], ["Wildlife1", "Wildlife2"])]
        self.deserts = [Desert("Desert1", "Description1", "Sand Dunes1", ["Oasis1", "Oasis2"])]
        self.oceans = [Ocean("Ocean1", "Description1", 5000, ["Marine Life1", "Marine Life2"])]

# Instantiate the WorldGeneration class to generate a world
world_gen = WorldGeneration()
for feature in world_gen.geographical_features:
    print(f"Geographical Feature: {feature.name}, Description: {feature.description}, Resources: {', '.join(feature.resources)}")

for biome in world_gen.biomes:
    print(f"Biome: {biome.name}, Description: {biome.description}, Flora: {', '.join(biome.flora)}, Fauna: {', '.join(biome.fauna)}")

for river in world_gen.rivers:
    print(f"River: {river.name}, Description: {river.description}, Length: {river.length} km, Fish Species: {', '.join(river.fish_species)}")

for mountain in world_gen.mountains:
    print(f"Mountain: {mountain.name}, Description: {mountain.description}, Height: {mountain.height} m, Mineral Resources: {', '.join(mountain.mineral_resources)}")

for forest in world_gen.forests:
    print(f"Forest: {forest.name}, Description: {forest.description}, Tree Species: {', '.join(forest.tree_species)}, Wildlife: {', '.join(forest.wildlife)}")

for desert in world_gen.deserts:
    print(f"Desert: {desert.name}, Description: {desert.description}, Sand Dunes: {desert.sand_dunes}, Oases: {', '.join(desert.oases)}")

for ocean in world_gen.oceans:
    print(f"Ocean: {ocean.name}, Description: {ocean.description}, Depth: {ocean.depth} m, Marine Life: {', '.join(ocean.marine_life)}")

class WeatherPattern:
    def __init__(self, name, description):
        self.name = name
        self.description = description


    def generate_weather_patterns(self):
        weather_patterns = [
            "Tropical Cyclone", "Thunderstorm", "Blizzard", "Heatwave", "Drought", "Flood", "Hailstorm", "Tornado",
            "Hurricane", "Monsoon", "Wildfire", "Sandstorm", "Snowstorm", "Rainstorm", "Windstorm", "Mist", "Fog",
            "Sleet", "Freeze", "Cold Wave", "Warm Front", "Cold Front", "High Pressure System", "Low Pressure System"
        ]
        return [random.choice(weather_patterns) for _ in range(random.randint(3, 10))]


class TerrainType:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def generate_terrain_types(self):
        terrain_types = [
            "Mountainous", "Hilly", "Flat", "Plateau", "Valley", "Canyon", "Basin", "Delta", "Coastal", "Desert",
            "Rainforest", "Savanna", "Grassland", "Wetland", "Tundra", "Taiga", "Alpine", "Volcanic", "Cave", "Underwater"
        ]
        return [random.choice(terrain_types) for _ in range(random.randint(3, 10))]


class Resource:
    def __init__(self, name, description, abundance):
        self.name = name
        self.description = description
        self.abundance = abundance

    def generate_resources(self):
        resources = [
            "Gold", "Silver", "Iron", "Coal", "Copper", "Diamonds", "Emeralds", "Sapphires", "Rubies", "Quartz",
            "Granite", "Marble", "Limestone", "Slate", "Gypsum", "Salt", "Phosphate", "Zinc", "Nickel", "Uranium",
            "Natural Gas", "Oil", "Geothermal Energy", "Wind Energy", "Solar Energy", "Hydroelectric Energy", "Biomass Energy",
            "Freshwater", "Fish", "Timber", "Fruit", "Vegetables", "Grains", "Livestock", "Poultry", "Seafood", "Spices", "Herbs"
        ]
        return [Resource(random.choice(resources), "A valuable resource", random.randint(1, 100)) for _ in range(random.randint(3, 10))]


class Flora:
    def __init__(self, name, description, habitat):
        self.name = name
        self.description = description
        self.habitat = habitat

    def generate_flora(self):
        flora_list = [
            "Oak Tree", "Pine Tree", "Cactus", "Fern", "Moss", "Bamboo", "Sagebrush", "Palm Tree", "Maple Tree", "Birch Tree",
            "Redwood Tree", "Sequoia Tree", "Mangrove Tree", "Eucalyptus Tree", "Baobab Tree", "Banyan Tree", "Willow Tree", "Cedar Tree",
            "Spruce Tree", "Fir Tree", "Hemlock Tree", "Cypress Tree", "Aspen Tree", "Cherry Tree", "Apple Tree", "Peach Tree", "Pear Tree",
            "Orange Tree", "Lemon Tree", "Lime Tree",             "Grapevine", "Olive Tree", "Banana Plant", "Mango Tree", "Papaya Tree", "Pineapple Plant", "Coffee Plant", "Tea Plant",
            "Cocoa Tree", "Rubber Tree", "Cinnamon Tree", "Pepper Plant", "Vanilla Orchid", "Saffron Crocus", "Lavender", "Rosemary",
            "Thyme", "Basil", "Mint", "Oregano", "Parsley", "Cilantro", "Chives", "Ginger", "Garlic", "Onion", "Lemongrass", "Rose",
            "Tulip", "Lily", "Orchid", "Sunflower", "Daisy", "Violet", "Peony", "Chrysanthemum", "Azalea", "Rhododendron"
        ]
        return [Flora(random.choice(flora_list), "A common type of flora", random.choice(["Forest", "Desert", "Mountain", "River", "Ocean"])) for _ in range(random.randint(3, 10))]


class Fauna:
    def __init__(self, name, description, habitat):
        self.name = name
        self.description = description
        self.habitat = habitat

    def generate_fauna(self):
        fauna_list = [
            "Deer", "Wolf", "Eagle", "Bear", "Fox", "Rabbit", "Snake", "Falcon", "Lynx", "Elk",
            "Moose", "Beaver", "Otter", "Badger", "Bison", "Cougar", "Panther", "Leopard", "Giraffe", "Elephant",
            "Rhino", "Hippopotamus", "Zebra", "Antelope", "Buffalo", "Gazelle", "Cheetah", "Hyena", "Kangaroo", "Koala",
            "Crocodile", "Alligator", "Komodo Dragon", "Iguana", "Chameleon", "Tortoise", "Sea Turtle", "Dolphin", "Whale",
            "Shark", "Octopus", "Jellyfish", "Starfish", "Seahorse", "Crab", "Lobster", "Shrimp", "Coral", "Seaweed",
            "Penguin", "Seagull", "Pelican", "Albatross", "Flamingo", "Swan", "Duck", "Goose", "Heron", "Crane",
            "Falcon", "Hawk", "Eagle", "Vulture", "Owl", "Parrot", "Hummingbird", "Peacock", "Sparrow", "Pigeon"
        ]
        return [Fauna(random.choice(fauna_list), "A common type of fauna", random.choice(["Forest", "Desert", "Mountain", "River", "Ocean"])) for _ in range(random.randint(3, 10))]


class Gameplay:
    def __init__(self):
        self.combat_factors = self.generate_combat_factors()
        self.exploration_factors = self.generate_exploration_factors()

    def generate_combat_factors(self):
        combat_factors = [
            "Weapon Type", "Armor Type", "Health Points", "Stamina", "Magic Points", "Skill Level", "Experience Points", "Attack Power",
            "Defense Power", "Speed", "Agility", "Critical Hit Chance", "Accuracy", "Evasion", "Elemental Resistance", "Status Resistance",
            "Terrain Advantage", "Weather Influence", "Day/Night Cycle Effects", "Morale", "Leadership", "Tactics", "Strategy", "Formation",
            "Alliance/Enemy Faction", "Reputation", "Fear Factor", "Surprise Attack Advantage", "Flanking Advantage", "High Ground Advantage",
            "Resource Management", "Supply Lines", "Logistics", "Siege Warfare", "Fortification", "Traps", "Ambush", "Reinforcements",
            "Mercenaries", "Allies", "Neutral Parties", "Diplomacy", "Negotiation", "Trade", "Espionage", "Sabotage", "Propaganda",
            "Psychological Warfare", "Biological Warfare", "Chemical Warfare", "Nuclear Warfare", "Guerrilla Warfare", "Conventional Warfare",
            "Asymmetric Warfare", "Cyber Warfare", "Space Warfare", "Underwater Warfare", "Air Warfare", "Land Warfare", "Sea Warfare",
            "Urban Warfare", "Jungle Warfare", "Desert Warfare", "Mountain Warfare", "Arctic Warfare", "Volcanic Warfare", "Extraterrestrial Warfare"
        ]
        return [random.choice(combat_factors) for _ in range(random.randint(10, 20))]

    def generate_exploration_factors(self):
        exploration_factors = [
            "Terrain Type", "Weather Conditions", "Day/Night Cycle", "Seasonal Changes", "Resource Availability", "Wildlife Encounters", "Flora Interactions",
            "Natural Disasters", "Environmental Hazards", "Hidden Treasures", "Lost Civilizations", "Ancient Ruins", "Mysterious Phenomena", "Secret Locations",
            "Underground Exploration", "Underwater Exploration", "Aerial Exploration", "Space Exploration", "Dimensional Exploration", "Time Travel",
            "Cultural Interactions", "Local Inhabitants", "Friendly Factions", "Hostile Factions", "Neutral Factions", "Trade Opportunities", "Diplomatic Engagements",
            "Scientific Research", "Archaeological Discoveries", "Historical Research", "Technological Advancements", "Magical Discoveries", "Religious Pilgrimages",
            "Spiritual Enlightenment", "Philosophical Insights", "Artistic Inspirations", "Musical Inspirations", "Literary Inspirations", "Culinary Discoveries",
            "Fashion Trends", "Sporting Events",             "Entertainment Opportunities", "Festivals", "Celebrations", "Ceremonies", "Traditions", "Customs", "Languages", "Religions",
            "Philosophies", "Government Systems", "Political Intrigues", "Economic Systems", "Social Hierarchies", "Cultural Exchanges",
            "Educational Opportunities", "Scientific Innovations", "Technological Innovations", "Magical Innovations", "Artistic Creations",
            "Musical Compositions", "Literary Works", "Theatrical Performances", "Cinematic Productions", "Television Productions",
            "Radio Productions", "Internet Productions", "Virtual Reality Experiences", "Augmented Reality Experiences", "Mixed Reality Experiences",
            "Simulation Experiences", "Game Experiences", "Sport Experiences", "Adventure Experiences", "Travel Experiences", "Tourism Experiences",
            "Culinary Experiences", "Fashion Experiences", "Wellness Experiences", "Spiritual Experiences", "Romantic Experiences", "Family Experiences",
            "Friendship Experiences", "Community Experiences", "Societal Experiences", "Global Experiences", "Galactic Experiences", "Universal Experiences",
            "Multidimensional Experiences", "Transcendental Experiences", "Mystical Experiences", "Paranormal Experiences", "Supernatural Experiences",
            "Extraordinary Experiences", "Unforgettable Experiences", "Life-Changing Experiences", "Mind-Expanding Experiences", "Soul-Enriching Experiences",
            "Heartwarming Experiences", "Inspiring Experiences", "Uplifting Experiences", "Empowering Experiences", "Transformative Experiences",
            "Healing Experiences", "Therapeutic Experiences", "Relaxing Experiences", "Rejuvenating Experiences", "Revitalizing Experiences",
            "Energizing Experiences", "Stimulating Experiences", "Exciting Experiences", "Thrilling Experiences", "Adrenaline-Pumping Experiences",
            "Heart-Stopping Experiences", "Breathtaking Experiences", "Awe-Inspiring Experiences", "Wonder-Inducing Experiences", "Amazement-Inducing Experiences",
            "Fascination-Inducing Experiences", "Intrigue-Inducing Experiences", "Curiosity-Inducing Experiences", "Discovery-Inducing Experiences",
            "Learning-Inducing Experiences", "Growth-Inducing Experiences", "Development-Inducing Experiences", "Progress-Inducing Experiences",
            "Innovation-Inducing Experiences", "Evolution-Inducing Experiences", "Revolution-Inducing Experiences", "Breakthrough-Inducing Experiences",
            "Pioneering Experiences", "Trailblazing Experiences", "Groundbreaking Experiences", "Record-Breaking Experiences", "History-Making Experiences",
            "Legacy-Creating Experiences", "Future-Shaping Experiences", "Destiny-Altering Experiences", "Fate-Changing Experiences", "Life-Defining Experiences",
            "Generation-Defining Experiences", "Era-Defining Experiences", "Age-Defining Experiences", "Millennium-Defining Experiences", "Eon-Defining Experiences",
            "Epoch-Defining Experiences", "Cosmic-Defining Experiences", "Universe-Defining Experiences", "Multiverse-Defining Experiences", "Existence-Defining Experiences",
            "Reality-Defining Experiences", "Dimension-Defining Experiences", "Space-Defining Experiences", "Time-Defining Experiences", "Matter-Defining Experiences",
            "Energy-Defining Experiences", "Force-Defining Experiences", "Power-Defining Experiences", "Authority-Defining Experiences", "Dominion-Defining Experiences",
            "Sovereignty-Defining Experiences", "Leadership-Defining Experiences", "Rulership-Defining Experiences", "Kingship-Defining Experiences", "Queenship-Defining Experiences",
            "Emperorship-Defining Experiences", "Empressship-Defining Experiences", "Presidency-Defining Experiences", "Premiership-Defining Experiences", "Chancellorship-Defining Experiences",
            "Governorship-Defining Experiences", "Mayorship-Defining Experiences", "Chiefship-Defining Experiences", "Captainship-Defining Experiences", "Commandership-Defining Experiences",
            "Generalship-Defining Experiences", "Admiralship-Defining Experiences", "Marshalship-Defining Experiences", "Commissionership-Defining Experiences", "Directorship-Defining Experiences",
            "Managership-Defining Experiences", "Supervisorship-Defining Experiences", "Coordinatorship-Defining Experiences", "Organizership-Defining Experiences", "Facilitatorship-Defining Experiences",
            "Mediatorship-Defining Experiences", "Negotiatorship-Defining Experiences", "Diplomatship-Defining Experiences", "Ambassadorship-Defining Experiences", "Consulship-Defining Experiences",
            "Envoyship-Defining Experiences", "Delegate-Defining Experiences", "Representative-Defining Experiences", "Spokespersonship-Defining Experiences", "Publicistship-Defining Experiences",
            "Promotership-Defining Experiences", "Marketership-Defining Experiences", "Advertisership-Defining Experiences", "Salesmanship-Defining Experiences", "Tradesmanship-Defining Experiences",
            "Craftsmanship-Defining Experiences", "Artisanship-Defining Experiences", "Mastership-Defining Experiences", "Expertship-Defining Experiences", "Specialistship-Defining Experiences",
            "Professionalship-Defining Experiences", "Technicianship-Defining Experiences", "Engineership-Defining Experiences", "Scientistship-Defining Experiences", "Researchership-Defining Experiences",
            "Scholarship-Defining Experiences", "Academicship-Defining Experiences", "Educatorship-Defining Experiences", "Teachership-Defining Experiences", "Professorship-Defining Experiences",
            "Doctorship-Defining Experiences", "Nursing-Defining Experiences", "Therapists-Defining Experiences", "Counselorship-Defining Experiences", "Advisership-Defining Experiences",
            "Consultantship-Defining Experiences", "Analystship-Defining Experiences", "Strategistship-Defining Experiences", "Plannership-Defining Experiences", "Developership-Defining Experiences",
            "Designership-Defining Experiences", "Architectship-Defining Experiences", "Buildership-Defining Experiences", "Constructorship-Defining Experiences",
            "Manufacturership-Defining Experiences", "Producership-Defining Experiences", "Directorship-Defining Experiences", "Creatorsship-Defining Experiences",
            "Inventorship-Defining Experiences", "Innovatorship-Defining Experiences", "Pioneer-Defining Experiences", "Trailblazer-Defining Experiences",
            "Groundbreaker-Defining Experiences", "Recordbreaker-Defining Experiences", "Champion-Defining Experiences", "Winner-Defining Experiences",
            "Victor-Defining Experiences", "Conqueror-Defining Experiences", "Master-Defining Experiences", "Hero-Defining Experiences", "Legend-Defining Experiences",
            "Icon-Defining Experiences", "Star-Defining Experiences", "Celebrity-Defining Experiences", "Superstar-Defining Experiences", "Megastar-Defining Experiences",
            "Rockstar-Defining Experiences", "Popstar-Defining Experiences", "Filmstar-Defining Experiences", "Sportstar-Defining Experiences", "Allstar-Defining Experiences",
            "Hall-of-Famer-Defining Experiences", "MVP-Defining Experiences", "GOAT-Defining Experiences", "Phenom-Defining Experiences", "Prodigy-Defining Experiences",
            "Genius-Defining Experiences", "Visionary-Defining Experiences", "Prophet-Defining Experiences", "Sage-Defining Experiences", "Guru-Defining Experiences",
            "Mastermind-Defining Experiences", "Wizard-Defining Experiences", "Sorcerer-Defining Experiences", "Magician-Defining Experiences", "Alchemist-Defining Experiences",
            "Philosopher-Defining Experiences", "Theologian-Defining Experiences", "Scholar-Defining Experiences", "Historian-Defining Experiences", "Biographer-Defining Experiences",
            "Novelist-Defining Experiences", "Poet-Defining Experiences", "Playwright-Defining Experiences", "Screenwriter-Defining Experiences", "Songwriter-Defining Experiences",
            "Composer-Defining Experiences", "Musician-Defining Experiences", "Singer-Defining Experiences", "Dancer-Defining Experiences", "Actor-Defining Experiences",
            "Performer-Defining Experiences", "Artist-Defining Experiences", "Painter-Defining Experiences", "Sculptor-Defining Experiences", "Photographer-Defining Experiences",
            "Filmmaker-Defining Experiences", "Director-Defining Experiences", "Producer-Defining Experiences", "Editor-Defining Experiences", "Critic-Defining Experiences",
            "Reviewer-Defining Experiences", "Commentator-Defining Experiences", "Analyst-Defining Experiences", "Correspondent-Defining Experiences", "Reporter-Defining Experiences",
            "Journalist-Defining Experiences", "Writer-Defining Experiences", "Author-Defining Experiences", "Publisher-Defining Experiences", "Broadcaster-Defining Experiences",
            "Podcaster-Defining Experiences", "Vlogger-Defining Experiences", "Blogger-Defining Experiences", "Influencer-Defining Experiences", "Streamer-Defining Experiences",
            "Gamer-Defining Experiences", "Designer-Defining Experiences", "Developer-Defining Experiences", "Programmer-Defining Experiences", "Coder-Defining Experiences",
            "Engineer-Defining Experiences", "Architect-Defining Experiences", "Builder-Defining Experiences", "Constructor-Defining Experiences", "Manufacturer-Defining Experiences",
            "Producer-Defining Experiences", "Marketer-Defining Experiences", "Advertiser-Defining Experiences", "Salesperson-Defining Experiences", "Trader-Defining Experiences",
            "Businessperson-Defining Experiences", "Entrepreneur-Defining Experiences", "Investor-Defining Experiences", "Financier-Defining Experiences", "Banker-Defining Experiences",
            "Economist-Defining Experiences", "Statistician-Defining Experiences", "Mathematician-Defining Experiences", "Scientist-Defining Experiences", "Researcher-Defining Experiences",
            "Inventor-Defining Experiences", "Innovator-Defining Experiences", "Pioneer-Defining Experiences", "Trailblazer-Defining Experiences", "Explorer-Defining Experiences",
            "Adventurer-Defining Experiences", "Traveler-Defining Experiences", "Tourist-Defining Experiences", "Voyager-Defining Experiences", "Pilgrim-Defining Experiences",
            "Wanderer-Defining Experiences", "Nomad-Defining Experiences", "Migrant-Defining Experiences", "Refugee-Defining Experiences", "Survivor-Defining Experiences",
            "Warrior-Defining Experiences", "Soldier-Defining Experiences", "Fighter-Defining Experiences", "Guardian-Defining Experiences", "Protector-Defining Experiences",
            "Defender-Defining Experiences", "Rescuer-Defining Experiences", "Savior-Defining Experiences", "Hero-Defining Experiences", "Champion-Defining Experiences",
            "Victor-Defining Experiences", "Conqueror-Defining Experiences", "Master-Defining Experiences", "Ruler-Defining Experiences", "Leader-Defining Experiences",
            "Commander-Defining Experiences", "General-Defining Experiences", "Admiral-Defining Experiences", "Marshal-Defining Experiences", "Emperor-Defining Experiences",
            "King-Defining Experiences", "Queen-Defining Experiences", "Prince-Defining Experiences", "Princess-Defining Experiences", "Duke-Defining Experiences",
            "Duchess-Defining Experiences", "Lord-Defining Experiences", "Lady-Defining Experiences", "Sir-Defining Experiences", "Dame-Defining Experiences",
            "Knight-Defining Experiences", "Baron-Defining Experiences", "Baroness-Defining Experiences", "Count-Defining Experiences", "Countess-Defining Experiences",
            "Viscount-Defining Experiences", "Viscountess-Defining Experiences",            "Viscount-Defining Experiences", "Viscountess-Defining Experiences", "Earl-Defining Experiences", "Marquess-Defining Experiences", "Marquis-Defining Experiences",
            "Marquise-Defining Experiences", "Archduke-Defining Experiences", "Archduchess-Defining Experiences", "Grand Duke-Defining Experiences", "Grand Duchess-Defining Experiences",
            "Pope-Defining Experiences", "Patriarch-Defining Experiences", "Matriarch-Defining Experiences", "Saint-Defining Experiences", "Prophet-Defining Experiences",
            "Sage-Defining Experiences", "Seer-Defining Experiences", "Oracle-Defining Experiences", "Shaman-Defining Experiences", "Witch-Defining Experiences",
            "Wizard-Defining Experiences", "Sorcerer-Defining Experiences", "Mage-Defining Experiences", "Magician-Defining Experiences", "Alchemist-Defining Experiences",
            "Druid-Defining Experiences", "Priest-Defining Experiences", "Priestess-Defining Experiences", "Monk-Defining Experiences", "Nun-Defining Experiences",
            "Friar-Defining Experiences", "Bishop-Defining Experiences", "Archbishop-Defining Experiences", "Cardinal-Defining Experiences", "Deacon-Defining Experiences",
            "Vicar-Defining Experiences", "Pastor-Defining Experiences", "Minister-Defining Experiences", "Reverend-Defining Experiences", "Chaplain-Defining Experiences",
            "Rabbi-Defining Experiences", "Imam-Defining Experiences", "Mufti-Defining Experiences", "Sheikh-Defining Experiences", "Ayatollah-Defining Experiences",
            "Lama-Defining Experiences", "Guru-Defining Experiences", "Swami-Defining Experiences", "Yogi-Defining Experiences", "Mystic-Defining Experiences",
            "Ascetic-Defining Experiences", "Hermit-Defining Experiences", "Recluse-Defining Experiences", "Sage-Defining Experiences", "Philosopher-Defining Experiences",
            "Scholar-Defining Experiences", "Academic-Defining Experiences", "Educator-Defining Experiences", "Teacher-Defining Experiences", "Mentor-Defining Experiences",
            "Tutor-Defining Experiences", "Coach-Defining Experiences", "Trainer-Defining Experiences", "Instructor-Defining Experiences", "Facilitator-Defining Experiences",
            "Guide-Defining Experiences", "Counselor-Defining Experiences", "Therapist-Defining Experiences", "Psychologist-Defining Experiences", "Psychotherapist-Defining Experiences",
            "Psychiatrist-Defining Experiences", "Analyst-Defining Experiences", "Consultant-Defining Experiences", "Advisor-Defining Experiences", "Expert-Defining Experiences",
            "Specialist-Defining Experiences", "Professional-Defining Experiences", "Technician-Defining Experiences", "Engineer-Defining Experiences", "Scientist-Defining Experiences",
            "Researcher-Defining Experiences", "Inventor-Defining Experiences", "Innovator-Defining Experiences", "Creator-Defining Experiences", "Artist-Defining Experiences",
            "Designer-Defining Experiences", "Craftsman-Defining Experiences", "Artisan-Defining Experiences", "Master-Defining Experiences", "Virtuoso-Defining Experiences",
            "Genius-Defining Experiences", "Visionary-Defining Experiences", "Pioneer-Defining Experiences", "Trailblazer-Defining Experiences", "Revolutionary-Defining Experiences",
            "Reformer-Defining Experiences", "Activist-Defining Experiences", "Advocate-Defining Experiences", "Campaigner-Defining Experiences", "Crusader-Defining Experiences",
            "Martyr-Defining Experiences", "Hero-Defining Experiences", "Savior-Defining Experiences", "Liberator-Defining Experiences", "Emancipator-Defining Experiences",
            "Abolitionist-Defining Experiences", "Rebel-Defining Experiences", "Insurgent-Defining Experiences", "Revolutionary-Defining Experiences", "Guerrilla-Defining Experiences",
            "Freedom Fighter-Defining Experiences", "Soldier-Defining Experiences", "Warrior-Defining Experiences", "Guardian-Defining Experiences", "Protector-Defining Experiences",
            "Defender-Defining Experiences", "Champion-Defining Experiences", "Victor-Defining Experiences", "Conqueror-Defining Experiences", "Master-Defining Experiences",
            "Ruler-Defining Experiences", "Leader-Defining Experiences", "King-Defining Experiences", "Queen-Defining Experiences", "Emperor-Defining Experiences",
            "Empress-Defining Experiences", "God-Defining Experiences", "Goddess-Defining Experiences", "Deity-Defining Experiences", "Supreme Being-Defining Experiences",
            "Creator-Defining Experiences", "Sustainer-Defining Experiences", "Destroyer-Defining Experiences", "Redeemer-Defining Experiences", "Savior-Defining Experiences",
            "Messiah-Defining Experiences", "Christ-Defining Experiences", "Buddha-Defining Experiences", "Prophet-Defining Experiences", "Saint-Defining Experiences",
            "Angel-Defining Experiences", "Archangel-Defining Experiences", "Seraphim-Defining Experiences", "Cherubim-Defining Experiences", "Spirit-Defining Experiences",
            "Soul-Defining Experiences", "Being-Defining Experiences", "Entity-Defining Experiences", "Existence-Defining Experiences", "Reality-Defining Experiences",
            "Universe-Defining Experiences", "Multiverse-Defining Experiences", "Omniverse-Defining Experiences", "Infinity-Defining Experiences", "Eternity-Defining Experiences",
            "Transcendence-Defining Experiences", "Enlightenment-Defining Experiences", "Nirvana-Defining Experiences", "Paradise-Defining Experiences",            "Heaven-Defining Experiences", "Utopia-Defining Experiences", "Shangri-La-Defining Experiences", "Valhalla-Defining Experiences", "Elysium-Defining Experiences",
            "Arcadia-Defining Experiences","Zion-Defining Experiences", "Olympus-Defining Experiences", "Asgard-Defining Experiences", "Atlantis-Defining Experiences", "Camelot-Defining Experiences",
            "Avalon-Defining Experiences", "El Dorado-Defining Experiences", "Xanadu-Defining Experiences", "Hyperborea-Defining Experiences", "Lemuria-Defining Experiences",
            "Mu-Defining Experiences", "Agartha-Defining Experiences", "Shambhala-Defining Experiences", "Nirvana-Defining Experiences", "Satori-Defining Experiences",
            "Samadhi-Defining Experiences", "Moksha-Defining Experiences", "Tao-Defining Experiences", "Zen-Defining Experiences", "Dharma-Defining Experiences",
            "Karma-Defining Experiences", "Yoga-Defining Experiences", "Meditation-Defining Experiences", "Prayer-Defining Experiences", "Worship-Defining Experiences",
            "Devotion-Defining Experiences", "Faith-Defining Experiences", "Belief-Defining Experiences"
        ]

class GameWorld:
    def __init__(self):
        self.experiences = [
            "Entertainment Opportunities", "Festivals", "Celebrations", "Ceremonies", "Traditions", "Customs", "Languages", "Religions",
            "Philosophies", "Government Systems", "Political Intrigues", "Economic Systems", "Social Hierarchies", "Cultural Exchanges",
            "Educational Opportunities", "Scientific Innovations", "Technological Innovations", "Magical Innovations", "Artistic Creations",
            "Musical Compositions", "Literary Works", "Theatrical Performances", "Cinematic Productions", "Television Productions",
            "Radio Productions", "Internet Productions", "Virtual Reality Experiences", "Augmented Reality Experiences", "Mixed Reality Experiences",
            "Simulation Experiences", "Game Experiences", "Sport Experiences", "Adventure Experiences", "Travel Experiences", "Tourism Experiences",
            "Culinary Experiences", "Fashion Experiences", "Wellness Experiences", "Spiritual Experiences", "Romantic Experiences", "Family Experiences",
            "Friendship Experiences", "Community Experiences", "Societal Experiences", "Global Experiences", "Galactic Experiences", "Universal Experiences",
            "Multidimensional Experiences", "Transcendental Experiences", "Mystical Experiences", "Paranormal Experiences", "Supernatural Experiences",
            "Extraordinary Experiences", "Unforgettable Experiences", "Life-Changing Experiences", "Mind-Expanding Experiences", "Soul-Enriching Experiences",
            "Heartwarming Experiences", "Inspiring Experiences", "Uplifting Experiences", "Empowering Experiences", "Transformative Experiences",
            "Healing Experiences", "Therapeutic Experiences", "Relaxing Experiences", "Rejuvenating Experiences", "Revitalizing Experiences",
            "Energizing Experiences", "Stimulating Experiences", "Exciting Experiences", "Thrilling Experiences", "Adrenaline-Pumping Experiences",
            "Heart-Stopping Experiences", "Breathtaking Experiences", "Awe-Inspiring Experiences", "Wonder-Inducing Experiences", "Amazement-Inducing Experiences",
            "Fascination-Inducing Experiences", "Intrigue-Inducing Experiences", "Curiosity-Inducing Experiences", "Discovery-Inducing Experiences",
            "Learning-Inducing Experiences", "Growth-Inducing Experiences", "Development-Inducing Experiences", "Progress-Inducing Experiences",
            "Innovation-Inducing Experiences", "Evolution-Inducing Experiences", "Revolution-Inducing Experiences", "Breakthrough-Inducing Experiences",
            "Pioneering Experiences", "Trailblazing Experiences", "Groundbreaking Experiences", "Record-Breaking Experiences", "History-Making Experiences",
            "Legacy-Creating Experiences", "Future-Shaping Experiences", "Destiny-Altering Experiences", "Fate-Changing Experiences", "Life-Defining Experiences",
            "Generation-Defining Experiences", "Era-Defining Experiences", "Age-Defining Experiences", "Millennium-Defining Experiences", "Eon-Defining Experiences",
            "Epoch-Defining Experiences", "Cosmic-Defining Experiences", "Universe-Defining Experiences", "Multiverse-Defining Experiences", "Existence-Defining Experiences",
            "Reality-Defining Experiences", "Dimension-Defining Experiences", "Space-Defining Experiences", "Time-Defining Experiences", "Matter-Defining Experiences",
            "Energy-Defining Experiences", "Force-Defining Experiences", "Power-Defining Experiences", "Authority-Defining Experiences", "Dominion-Defining Experiences",
            "Sovereignty-Defining Experiences", "Leadership-Defining Experiences", "Rulership-Defining Experiences", "Kingship-Defining Experiences", "Queenship-Defining Experiences",
            "Emperorship-Defining Experiences", "Empressship-Defining Experiences", "Presidency-Defining Experiences", "Premiership-Defining Experiences", "Chancellorship-Defining Experiences",
            "Governorship-Defining Experiences", "Mayorship-Defining Experiences", "Chiefship-Defining Experiences", "Captainship-Defining Experiences", "Commandership-Defining Experiences",
            "Generalship-Defining Experiences", "Admiralship-Defining Experiences", "Marshalship-Defining Experiences", "Commissionership-Defining Experiences", "Directorship-Defining Experiences",
            "Managership-Defining Experiences", "Supervisorship-Defining Experiences", "Coordinatorship-Defining Experiences", "Organizership-Defining Experiences", "Facilitatorship-Defining Experiences",
            "Mediatorship-Defining Experiences", "Negotiatorship-Defining Experiences", "Diplomatship-Defining Experiences", "Ambassadorship-Defining Experiences", "Consulship-Defining Experiences",
            "Envoyship-Defining Experiences", "Delegate-Defining Experiences", "Representative-Defining Experiences", "Spokespersonship-Defining Experiences", "Publicistship-Defining Experiences",
            "Promotership-Defining Experiences", "Marketership-Defining Experiences", "Advertisership-Defining Experiences", "Salesmanship-Defining Experiences", 
            "Entrepreneurship-Defining Experiences", "Innovatorship-Defining Experiences", "Pioneership-Defining Experiences", "Visionaryship-Defining Experiences", 
            "Leadership-Defining Experiences", "Mentorship-Defining Experiences", "Coachship-Defining Experiences", "Teacher-Defining Experiences", 
            "Educatorship-Defining Experiences", "Scholarship-Defining Experiences", "Researchership-Defining Experiences", "Scientistship-Defining Experiences", 
            "Engineership-Defining Experiences", "Technicianship-Defining Experiences", "Craftsmanship-Defining Experiences", "Artistry-Defining Experiences", 
            "Mastership-Defining Experiences", "Expertship-Defining Experiences", "Professionalship-Defining Experiences", "Specialistship-Defining Experiences", 
            "Guru-Defining Experiences", "Wizardship-Defining Experiences", "Geniusship-Defining Experiences", "Prodigyship-Defining Experiences", 
            "Virtuosoship-Defining Experiences", "Maestroship-Defining Experiences", "Champion-Defining Experiences", "Hero-Defining Experiences", 
            "Legend-Defining Experiences", "Icon-Defining Experiences", "Star-Defining Experiences", "Superstar-Defining Experiences", 
            "Megastar-Defining Experiences", "Luminary-Defining Experiences", "Celebrity-Defining Experiences", "VIP-Defining Experiences", 
            "MVP-Defining Experiences", "GOAT-Defining Experiences", "Hall-of-Famer-Defining Experiences", "Trailblazer-Defining Experiences", 
            "Pioneer-Defining Experiences", "Innovator-Defining Experiences", "Revolutionary-Defining Experiences", "Game-Changer-Defining Experiences", 
            "Change-Maker-Defining Experiences", "Influencer-Defining Experiences", "Leader-Defining Experiences", "Visionary-Defining Experiences", 
            "Titan-Defining Experiences", "Giant-Defining Experiences", "Colossus-Defining Experiences", "Behemoth-Defining Experiences", 
            "Leviathan-Defining Experiences", "Monolith-Defining Experiences", "Goliath-Defining Experiences", "Juggernaut-Defining Experiences", 
            "Powerhouse-Defining Experiences", "Dynamo-Defining Experiences", "Force-Defining Experiences", "Phenomenon-Defining Experiences", 
            "Wonder-Defining Experiences", "Marvel-Defining Experiences", "Sensation-Defining Experiences", "Miracle-Defining Experiences", 
            "Prodigy-Defining Experiences", "Genius-Defining Experiences", "Mastermind-Defining Experiences", "Mogul-Defining Experiences", 
            "Tycoon-Defining Experiences", "Baron-Defining Experiences", "Magnate-Defining Experiences", "Dignitary-Defining Experiences", 
            "Noble-Defining Experiences", "Royalty-Defining Experiences", "Monarch-Defining Experiences", "Sovereign-Defining Experiences", 
            "Ruler-Defining Experiences", "Emperor-Defining Experiences", "Empress-Defining Experiences", "King-Defining Experiences", 
            "Queen-Defining Experiences", "Prince-Defining Experiences", "Princess-Defining Experiences", "Duke-Defining Experiences", 
            "Duchess-Defining Experiences", "Lord-Defining Experiences", "Lady-Defining Experiences", "Sir-Defining Experiences", 
            "Dame-Defining Experiences", "Knight-Defining Experiences", "Baronet-Defining Experiences", "Count-Defining Experiences", 
            "Countess-Defining Experiences", "Viscount-Defining Experiences", "Viscountess-Defining Experiences", "Earl-Defining Experiences", 
            "Marquess-Defining Experiences", "Marquis-Defining Experiences", "Marquise-Defining Experiences", "Archduke-Defining Experiences", 
            "Archduchess-Defining Experiences", "Grand Duke-Defining Experiences", "Grand Duchess-Defining Experiences", "Pope-Defining Experiences", 
            "Patriarch-Defining Experiences", "Matriarch-Defining Experiences", "Saint-Defining Experiences", "Prophet-Defining Experiences", 
            "Sage-Defining Experiences", "Seer-Defining Experiences", "Oracle-Defining Experiences", "Shaman-Defining Experiences", 
            "Witch-Defining Experiences", "Wizard-Defining Experiences", "Sorcerer-Defining Experiences", "Mage-Defining Experiences", 
            "Magician-Defining Experiences", "Alchemist-Defining Experiences", "Druid-Defining Experiences", "Priest-Defining Experiences", 
            "Priestess-Defining Experiences", "Monk-Defining Experiences", "Nun-Defining Experiences", "Friar-Defining Experiences", 
            "Bishop-Defining Experiences", "Archbishop-Defining Experiences", "Cardinal-Defining Experiences", "Deacon-Defining Experiences", 
            "Vicar-Defining Experiences", "Pastor-Defining Experiences", "Minister-Defining Experiences", "Reverend-Defining Experiences", 
            "Chaplain-Defining Experiences", "Rabbi-Defining Experiences", "Imam-Defining Experiences", "Mufti-Defining Experiences", 
            "Sheikh-Defining Experiences", "Ayatollah-Defining Experiences", "Lama-Defining Experiences", "Guru-Defining Experiences", 
            "Swami-Defining Experiences", "Yogi-Defining Experiences", "Mystic-Defining Experiences", "Ascetic-Defining Experiences", 
            "Hermit-Defining Experiences", "Recluse-Defining Experiences", "Sage-Defining Experiences", "Philosopher-Defining Experiences", 
            "Scholar-Defining Experiences", "Academic-Defining Experiences", "Educator-Defining Experiences",
            "Teacher-Defining Experiences", "Mentor-Defining Experiences", "Tutor-Defining Experiences", "Coach-Defining Experiences", 
            "Trainer-Defining Experiences", "Instructor-Defining Experiences", "Facilitator-Defining Experiences", "Guide-Defining Experiences", 
            "Counselor-Defining Experiences", "Therapist-Defining Experiences", "Psychologist-Defining Experiences", "Psychotherapist-Defining Experiences", 
            "Psychiatrist-Defining Experiences", "Analyst-Defining Experiences", "Consultant-Defining Experiences", "Advisor-Defining Experiences", 
            "Expert-Defining Experiences", "Specialist-Defining Experiences", "Professional-Defining Experiences", "Technician-Defining Experiences", 
            "Engineer-Defining Experiences", "Scientist-Defining Experiences", "Researcher-Defining Experiences", "Inventor-Defining Experiences", 
            "Innovator-Defining Experiences", "Creator-Defining Experiences", "Artist-Defining Experiences", "Designer-Defining Experiences", 
            "Craftsman-Defining Experiences", "Artisan-Defining Experiences", "Master-Defining Experiences", "Virtuoso-Defining Experiences", 
            "Genius-Defining Experiences", "Visionary-Defining Experiences", "Pioneer-Defining Experiences", "Trailblazer-Defining Experiences", 
            "Revolutionary-Defining Experiences", "Reformer-Defining Experiences", "Activist-Defining Experiences", "Advocate-Defining Experiences", 
            "Campaigner-Defining Experiences", "Crusader-Defining Experiences", "Martyr-Defining Experiences", "Hero-Defining Experiences", 
            "Savior-Defining Experiences", "Liberator-Defining Experiences", "Emancipator-Defining Experiences", "Abolitionist-Defining Experiences", 
            "Rebel-Defining Experiences", "Insurgent-Defining Experiences", "Revolutionary-Defining Experiences", "Guerrilla-Defining Experiences", 
            "Freedom Fighter-Defining Experiences", "Soldier-Defining Experiences", "Warrior-Defining Experiences", "Guardian-Defining Experiences", 
            "Protector-Defining Experiences", "Defender-Defining Experiences", "Champion-Defining Experiences", "Victor-Defining Experiences", 
            "Conqueror-Defining Experiences", "Master-Defining Experiences", "Ruler-Defining Experiences", "Leader-Defining Experiences", 
            "King-Defining Experiences", "Queen-Defining Experiences", "Emperor-Defining Experiences", "Empress-Defining Experiences", 
            "God-Defining Experiences", "Goddess-Defining Experiences", "Deity-Defining Experiences", "Supreme Being-Defining Experiences", 
            "Creator-Defining Experiences", "Sustainer-Defining Experiences", "Destroyer-Defining Experiences", "Redeemer-Defining Experiences", 
            "Savior-Defining Experiences", "Messiah-Defining Experiences", "Christ-Defining Experiences", "Buddha-Defining Experiences", 
            "Prophet-Defining Experiences", "Saint-Defining Experiences", "Angel-Defining Experiences", "Archangel-Defining Experiences", 
            "Seraphim-Defining Experiences", "Cherubim-Defining Experiences", "Spirit-Defining Experiences", "Soul-Defining Experiences", 
            "Being-Defining Experiences", "Entity-Defining Experiences", "Existence-Defining Experiences", "Reality-Defining Experiences", 
            "Universe-Defining Experiences", "Multiverse-Defining Experiences", "Omniverse-Defining Experiences", "Infinity-Defining Experiences", 
            "Eternity-Defining Experiences", "Transcendence-Defining Experiences", "Enlightenment-Defining Experiences", "Nirvana-Defining Experiences", 
            "Paradise-Defining Experiences", "Heaven-Defining Experiences", "Utopia-Defining Experiences", "Shangri-La-Defining Experiences", 
            "Valhalla-Defining Experiences", "Elysium-Defining Experiences", "Arcadia-Defining Experiences", "Eden-Defining Experiences", 
            "Zion-Defining Experiences", "Olympus-Defining Experiences", "Asgard-Defining Experiences", "Atlantis-Defining Experiences", 
            "Camelot-Defining Experiences", "Avalon-Defining Experiences", "El Dorado-Defining Experiences", "Xanadu-Defining Experiences", 
            "Hyperborea-Defining Experiences", "Lemuria-Defining Experiences", "Mu-Defining Experiences", "Agartha-Defining Experiences", 
            "Shambhala-Defining Experiences", "Nirvana-Defining Experiences", "Satori-Defining Experiences", "Samadhi-Defining Experiences", 
            "Moksha-Defining Experiences", "Tao-Defining Experiences", "Zen-Defining Experiences", "Dharma-Defining Experiences", 
            "Karma-Defining Experiences", "Yoga-Defining Experiences", "Meditation-Defining Experiences", "Prayer-Defining Experiences", 
            "Worship-Defining Experiences", "Devotion-Defining Experiences", "Faith-Defining Experiences", "Belief-Defining Experiences", 
            "Hope-Defining Experiences", "Love-Defining Experiences"
        ]

class WorldGenerator:
    def __init__(self):
        self.regions = ["Mystic Forest", "Ancient Ruins", "Bustling City", "Tranquil Beach", "Snowy Mountains", "Enchanted Valley"]
        self.experiences = [
            "Worship-Defining Experiences", "Devotion-Defining Experiences", 
            "Faith-Defining Experiences", "Belief-Defining Experiences", 
            "Hope-Defining Experiences", "Love-Defining Experiences"
        ]

    def generate_world(self):
        world = {}
        for region in self.regions:
            world[region] = {
                "description": self.generate_description(region),
                "events": self.generate_events(),
                "npcs": self.generate_npcs(),
                "experiences": random.sample(self.experiences, k=20),
                "items": self.generate_items(),
                "quests": self.generate_quests(),
                "monsters": self.generate_monsters()
            }
        return world

    def generate_description(self, region):
        descriptions = {
            "Mystic Forest": "A forest filled with ancient trees and glowing plants. Mystical creatures roam freely here.",
            "Ancient Ruins": "Ruins of an ancient civilization, holding secrets and treasures waiting to be discovered.",
            "Bustling City": "A vibrant city with a mix of modern and traditional architecture, where various NPCs gather.",
            "Tranquil Beach": "A peaceful beach with golden sands and clear waters, a place for relaxation and exploration.",
            "Snowy Mountains": "A region covered in snow and ice, home to many dangerous creatures and hidden caves.",
            "Enchanted Valley": "A valley filled with magical flora and fauna, a place where many adventures await."
        }
        return descriptions.get(region, "Unknown Region")

    def generate_events(self):
        # Implement this method to generate events
        return ["Sample Event"]

    def generate_npcs(self):
        # Implement this method to generate NPCs
        return ["Sample NPC"]

    def generate_items(self):
        # Implement this method to generate items
        return ["Sample Item"]

    def generate_quests(self):
        # Implement this method to generate quests
        return ["Sample Quest"]

    def generate_monsters(self):
        # Implement this method to generate monsters
        return ["Sample Monster"]

# Example usage:
world_gen = WorldGenerator()
generated_world = world_gen.generate_world()
print(generated_world)


def generate_description(self, region):
    descriptions = {
        "Mystic Forest": "A forest filled with ancient trees and glowing plants. Mystical creatures roam freely here.",
        "Ancient Ruins": "Ruins of an ancient civilization, holding secrets and treasures waiting to be discovered.",
        "Bustling City": "A vibrant city with a mix of modern and traditional architecture, where various NPCs gather.",
        "Tranquil Beach": "A peaceful beach with golden sands and clear waters, a place for relaxation and exploration.",
        "Snowy Mountains": "A region covered in snow and ice, home to many dangerous creatures and hidden caves.",
        "Enchanted Valley": "A valley filled with magical flora and fauna, a place where many adventures await."
    }
    return descriptions.get(region, "A place filled with wonders and dangers.")

def generate_events(self):
    return random.sample(self.events, k=random.randint(2, 4))

def generate_npcs(self):
    return random.sample(self.npcs, k=random.randint(2, 4))

def generate_items(self):
    items = [
        "Mystic Potion", "Ancient Sword", "Golden Shield", 
        "Enchanted Ring", "Crystal Ball", "Healing Herb", 
        "Magic Wand", "Silver Dagger", "Treasure Map", 
        "Dragon Scale Armor", "Phoenix Feather", "Unicorn Horn"
    ]
    return random.sample(items, k=random.randint(3, 6))

def generate_quests(self):
    quests = [
        "Rescue the captured princess", "Find the hidden treasure", 
        "Defeat the dragon terrorizing the village", "Collect rare herbs for the healer", 
        "Solve the riddles of the ancient oracle", "Help the merchant establish trade routes", 
        "Retrieve the stolen artifact", "Explore the haunted ruins", 
        "Win the grand tournament", "Protect the village from bandit attacks"
    ]
    return random.sample(quests, k=random.randint(2, 5))

def generate_monsters(self):
    monsters = [
        "Fire Dragon", "Ice Phoenix", "Stone Golem", 
        "Shadow Demon", "Thunder Griffin", "Wind Serpent", 
        "Water Kraken", "Earth Centaur", "Light Unicorn", 
        "Dark Vampire", "Metal Cyclops", "Wood Elf"
    ]
    return random.sample(monsters, k=random.randint(3, 6))


import random

class GameWorld:
    def __init__(self):
        self.experiences = [f"Experience {i}" for i in range(1, 101)]  # Generating a list of 100 experiences
        self.regions = [
            "Mystic Forest", "Ancient Ruins", "Bustling City", 
            "Tranquil Beach", "Snowy Mountains", "Enchanted Valley"
        ]
        self.events = [
            "Festival of Lights", "Grand Tournament", "Royal Coronation", 
            "Mystical Convergence", "Harvest Celebration", "Winter Solstice"
        ]
        self.npcs = [
            "Wise Sage", "Valiant Knight", "Mysterious Sorcerer", 
            "Kind Healer", "Resourceful Merchant", "Enigmatic Oracle"
        ]
        self.world = self.generate_world()

    def generate_world(self):
        world = {}
        for region in self.regions:
            world[region] = {
                "description": self.generate_description(region),
                "events": self.generate_events(),
                "npcs": self.generate_npcs(),
                "experiences": random.sample(self.experiences, k=20),
                "items": self.generate_items(),
                "quests": self.generate_quests(),
                "monsters": self.generate_monsters()
            }
        return world

    # ... (include the generate_description, generate_events, generate_npcs, generate_items, generate_quests, generate_monsters methods here)

    def display_world(self):
        for region, details in self.world.items():
            print(f"Region: {region}")
            print(f"  Description: {details['description']}")
            print(f"  Events: {', '.join(details['events'])}")
            print(f"  NPCs: {', '.join(details['npcs'])}")
            print(f"  Experiences: {', '.join(details['experiences'])}")
            print(f"  Items: {', '.join(details['items'])}")
            print(f"  Quests: {', '.join(details['quests'])}")
            print(f"  Monsters: {', '.join(details['monsters'])}")

class Player:
    def __init__(self):
        self.experience_points = 0
        self.current_experience = None
        self.inventory = []
        self.location = None
        self.health = 100
        self.level = 1

    def gain_experience(self, experience):
        self.current_experience = experience
        self.experience_points += 10
        self.level_up()

    def level_up(self):
        if self.experience_points >= 100:
            self.level += 1
            self.experience_points = 0
            print(f"You leveled up! You are now level {self.level}")

    def display_status(self):
        print(f"Current Experience: {self.current_experience}")
        print(f"Experience Points: {self.experience_points}")
        print(f"Current Location: {self.location}")
        print(f"Inventory: {', '.join(self.inventory)}")
        print(f"Health: {self.health}")
        print(f"Level: {self.level}")

    def travel(self, location):
        self.location = location
        print(f"You have traveled to {location}")

    def collect_item(self, item):
        self.inventory.append(item)
        print(f"You have collected {item}")

def main():
    world = GameWorld()
    player = Player()

    # Simulate the player gaining a random experience from the world
    random_experience = random.choice(world.experiences)
    player.gain_experience(random_experience)

    # Simulate the player traveling to a random location
    random_location = random.choice(world.regions)
    player.travel(random_location)

    # Simulate the player collecting a random item
    random_item = random.choice(world.world[random_location]['items'])
    player.collect_item(random_item)

    # Display the player's status
    player.display_status()

if __name__ == "__main__":
    main()











