# Lesson 9 Training: operator overloading, __add__

# Lesson 9 Training:
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"Galleons: {self.galleons} - Sickles: {self.sickles} - Knuts: {self.knuts}"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

new_galleons = potter.galleons + weasley.galleons

# ❗__init__(self, ...) 的意思：

# total = Vault()
# Vault.__init__(total, new_galleons, 5, 5) 對應 def __init__(self, galleons=0, sickles=0, knuts=0) 的格式
# 等於 total = Vault(new_galleons, 5, 5) 可讀性更高，pythonic

# total = Vault(new_galleons, 5, 5)

# ---------------------------------------------------------------------------

# ❗total = potter.__add__(weasley) 的意思：

# 等於 total = Vault.__add__(potter, weasley) 對應 def __add__(self, other) 的格式
# 等於 total = potter + weasley 可讀性更高，pythonic

# total = potter + weasley
total = Vault.__add__(potter, weasley)
print(total)
