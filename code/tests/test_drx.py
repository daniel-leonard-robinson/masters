from test_ import *

descr = '30_2'

@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'drx/'

# @pytest.mark.skip()
def test_drx_set(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    setEDRX(4, 1, 2, 2, 6, 2) # 2.56 continuous
    capture(1)

def test_drx_cap(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    # capture(12)
    capture()