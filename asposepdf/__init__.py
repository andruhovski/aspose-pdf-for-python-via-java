import jpype
import os

__asposepdf_dir__ = os.path.dirname(__file__)
__asposepdf_jar_path__ = __asposepdf_dir__ + "/javalib/aspose.pdf-22.4.jar"
jpype.addClassPath("__asposepdf_jar_path__")
jpype.startJVM(jpype.getDefaultJVMPath())
