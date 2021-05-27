import random

fn = ('赵', '钱', '孙', '李')
ln1 = ('东', '西', '南', '北')
ln2 = ('子鼠', '丑牛', '寅虎', '卯兔')


class FakeUser:
    def fake_name(self, random1):

        if random1 == 1:
            full_name = random.choice(fn) + random.choice(ln1)
        elif random1 == 2:
            full_name = random.choice(fn) + random.choice(ln2)
        else:
            full_name = random.choice(fn) + random.choice(ln1) + random.choice(ln2)

        gender = random.choice(['男', '女', '阴阳人'])
        print(full_name, ' ', gender.rjust(0),end=' ')


class SnsUser(FakeUser):
    def get_followers(self, few=True):
        if few:
            followers = random.randrange(1, 50)
        else:
            followers = random.randrange(200, 10000)
        print(repr(followers).rjust(4))


# 实例化
user_a = FakeUser()
user_b = SnsUser()
# 调用
# user_a.fake_name(random.randint(1, 4))
# user_b.get_followers(random.choice([True, False]))
for i in range(50):
    # print(user_b.fake_name(random.choice([1, 2, 3])).rjust(0), ',', user_b.get_followers(random.choice([True, False])))
    user_b.fake_name(random.choice([1, 2, 3]))
    user_b.get_followers(random.choice([True, False]))
