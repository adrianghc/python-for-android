from pythonforandroid.recipe import PythonRecipe
from pythonforandroid.logger import info
import zipfile
from pythonforandroid.toolchain import shprint
import sh

class ShibokenRecipe(PythonRecipe):
    version = '6.3.1'
    wheel_path = '/home/adrianghc/wheels/shiboken6-6.3.1-6.3.1-cp36-abi3-android_x86_64.whl'

    call_hostpython_via_targetpython = False
    install_in_hostpython = False

    def build_arch(self, arch):
        ''' Unzip the wheel and copy into site-packages of target'''
        env = self.get_recipe_env(arch)
        info('Shyam Experimentation')
        info('ENV: {}'.format("\n".join("export {}='{}'".format(n, v) for n, v in env.items())))
        shprint(sh.echo, '$PATH', _env=env)
        shprint(sh.echo, '$LDFLAGS', _env=env)
        shprint(sh.echo, '$CFLAGS', _env=env)
        print(env)

        info('Installing {} into site-packages'.format(self.name))
        with zipfile.ZipFile(self.wheel_path, 'r') as zip_ref:
            info('Unzip wheels and copy into {}'.format(self.ctx.get_python_install_dir(arch.arch)))
            zip_ref.extractall(self.ctx.get_python_install_dir(arch.arch))

recipe = ShibokenRecipe()
