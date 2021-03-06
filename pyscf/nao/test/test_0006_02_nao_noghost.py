# Copyright 2014-2018 The PySCF Developers. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function, division
import unittest

class KnowValues(unittest.TestCase):

    def test_0006_02_nao_noghost(self):
        import os
        from pyscf.nao import nao
        from pyscf.nao.m_overlap_am import overlap_am

        dname = os.path.join(os.path.split(__file__)[0], 'test_ag13_noghost')
        sv = nao(label='siesta', cd=dname)
        aa = sv.vna_coo().toarray()
        oc = sv.overlap_check(funct=overlap_am)
        self.assertTrue(oc[0])
    

if __name__ == "__main__": 
    unittest.main()
