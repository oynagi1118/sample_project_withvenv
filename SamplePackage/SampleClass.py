from SamplePackage.World import World


class SampleClass:
    def hello(self):
        world = World()
        ret = world.say('hello world')
        return ret is len('hello world');
