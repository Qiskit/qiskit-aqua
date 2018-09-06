# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
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
# =============================================================================
import unittest

import numpy as np

from qiskit_aqua import run_algorithm
from qiskit_aqua.input import get_input_instance
from test.common import QiskitAquaTestCase


class TestSVMClassical(QiskitAquaTestCase):
    def setUp(self):
        pass

    def test_classical_binary(self):
        training_input = {'A': np.asarray([[0.6560706, 0.17605998],
                                           [0.25776033, 0.47628296],
                                           [0.79687342, 0.26933706],
                                           [0.39016555, -0.08469916],
                                           [0.3994399, 0.13601573],
                                           [0.26752049, -0.03978988],
                                           [0.24026485, 0.01953518],
                                           [0.49490503, 0.17239737],
                                           [0.70171827, 0.5323737],
                                           [0.43221576, 0.42357294],
                                           [0.62864856, 0.45504447],
                                           [0.6259567, 0.30917324],
                                           [0.58272403, 0.20760754],
                                           [0.3938784, 0.17184466],
                                           [0.14154948, 0.06201424],
                                           [0.80202323, 0.40582692],
                                           [0.46779595, 0.39946754],
                                           [0.57660199, 0.21821317],
                                           [0.51044761, 0.03699459],
                                           [0.8690704, 0.70847635]]),
                          'B': np.asarray([[0.38857596, -0.33775802],
                                           [0.49946978, -0.48727951],
                                           [-0.30119743, -0.11221681],
                                           [-0.16479252, -0.08640519],
                                           [-0.21808884, -0.56508327],
                                           [-0.14683258, -0.46528508],
                                           [-0.05888195, -0.51474852],
                                           [0.20517435, -0.66839091],
                                           [0.25475584, -0.21239966],
                                           [0.55194854, 0.02789679],
                                           [-0.11542951, -0.54157026],
                                           [0.44625538, -0.49485869],
                                           [-0.14609118, -0.60719757],
                                           [0.18121305, -0.1922198],
                                           [0.19283785, -0.31798925],
                                           [0.29626405, -0.54563098],
                                           [-0.39044304, -0.36527253],
                                           [-0.29432215, -0.43924164],
                                           [-0.40294517, -0.31381308],
                                           [0.49156185, -0.3660534]])}

        test_input = {'A': np.asarray([[0.57483139, 0.47120732],
                                       [0.48372348, 0.25438544],
                                       [0.08791134, 0.11515506],
                                       [0.45988094, 0.32854319],
                                       [0.53015085, 0.41539212],
                                       [0.5073321, 0.47346751],
                                       [0.71081819, 0.19202569],
                                       [1., 0.51698289],
                                       [0.630973, 0.19898666],
                                       [0.48142649, 0.15931707]]),
                      'B': np.asarray([[-0.06048935, -0.48345293],
                                       [-0.01065613, -0.33910828],
                                       [-0.17323832, -0.49535592],
                                       [0.14043268, -0.87869109],
                                       [-0.15046837, -0.47340207],
                                       [-0.39600934, -0.21647957],
                                       [-0.394202, -0.44705385],
                                       [0.15243621, -0.36695163],
                                       [0.06195634, -0.23262325],
                                       [0.06183066, -0.53376975]])}

        temp = [test_input[k] for k in test_input]
        total_array = np.concatenate(temp)

        params = {
            'problem': {'name': 'svm_classification'},
            'algorithm': {
                'name': 'SVM',
            }
        }

        algo_input = get_input_instance('SVMInput')
        algo_input.training_dataset = training_input
        algo_input.test_dataset = test_input
        algo_input.datapoints = total_array

        result = run_algorithm(params, algo_input)
        self.assertEqual(result['testing_accuracy'], 1.0)
        self.assertEqual(result['predicted_classes'],
                         ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
                          'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])

    def test_classical_multiclass_one_against_all(self):
        training_input = {'A': np.asarray([[0.6560706, 0.17605998],
                                           [0.25776033, 0.47628296],
                                           [0.79687342, 0.26933706],
                                           [0.39016555, -0.08469916],
                                           [0.3994399, 0.13601573],
                                           [0.26752049, -0.03978988],
                                           [0.24026485, 0.01953518],
                                           [0.49490503, 0.17239737],
                                           [0.70171827, 0.5323737],
                                           [0.43221576, 0.42357294],
                                           [0.62864856, 0.45504447],
                                           [0.6259567, 0.30917324],
                                           [0.58272403, 0.20760754],
                                           [0.3938784, 0.17184466],
                                           [0.14154948, 0.06201424],
                                           [0.80202323, 0.40582692],
                                           [0.46779595, 0.39946754],
                                           [0.57660199, 0.21821317],
                                           [0.51044761, 0.03699459],
                                           [0.8690704, 0.70847635]]),
                          'B': np.asarray([[0.38857596, -0.33775802],
                                           [0.49946978, -0.48727951],
                                           [-0.30119743, -0.11221681],
                                           [-0.16479252, -0.08640519],
                                           [-0.21808884, -0.56508327],
                                           [-0.14683258, -0.46528508],
                                           [-0.05888195, -0.51474852],
                                           [0.20517435, -0.66839091],
                                           [0.25475584, -0.21239966],
                                           [0.55194854, 0.02789679],
                                           [-0.11542951, -0.54157026],
                                           [0.44625538, -0.49485869],
                                           [-0.14609118, -0.60719757],
                                           [0.18121305, -0.1922198],
                                           [0.19283785, -0.31798925],
                                           [0.29626405, -0.54563098],
                                           [-0.39044304, -0.36527253],
                                           [-0.29432215, -0.43924164],
                                           [-0.40294517, -0.31381308],
                                           [0.49156185, -0.3660534]]),
                          'C': np.asarray([[-0.68088231, 0.46824423],
                                           [-0.56167659, 0.65270294],
                                           [-0.54323753, 0.67630888],
                                           [-0.57685569, -0.08515631],
                                           [-0.67765364, 0.19654347],
                                           [-0.62129115, 0.22223066],
                                           [-0.78040851, 0.65247848],
                                           [-0.50730279, 0.59898039],
                                           [-0.64275805, 0.63381998],
                                           [-0.72854201, 0.14151325],
                                           [-0.57004437, 0.12344874],
                                           [-0.55215973, 0.74331215],
                                           [-0.60916047, 0.52006917],
                                           [-0.23093745, 1.],
                                           [-0.84025337, 0.5564536],
                                           [-0.66952391, 0.57918859],
                                           [-0.67725082, 0.60439934],
                                           [-1., 0.23715261],
                                           [-0.62933025, 0.19055405],
                                           [-0.82139073, 0.29941512]])}

        test_input = {'A': np.asarray([[0.57483139, 0.47120732],
                                       [0.48372348, 0.25438544],
                                       [0.08791134, 0.11515506],
                                       [0.45988094, 0.32854319],
                                       [0.53015085, 0.41539212],
                                       [0.5073321, 0.47346751],
                                       [0.71081819, 0.19202569],
                                       [1., 0.51698289],
                                       [0.630973, 0.19898666],
                                       [0.48142649, 0.15931707]]),
                      'B': np.asarray([[-0.06048935, -0.48345293],
                                       [-0.01065613, -0.33910828],
                                       [-0.17323832, -0.49535592],
                                       [0.14043268, -0.87869109],
                                       [-0.15046837, -0.47340207],
                                       [-0.39600934, -0.21647957],
                                       [-0.394202, -0.44705385],
                                       [0.15243621, -0.36695163],
                                       [0.06195634, -0.23262325],
                                       [0.06183066, -0.53376975]]),
                      'C': np.asarray([[-0.74561108, 0.27047295],
                                       [-0.69942965, 0.11885162],
                                       [-0.52649891, 0.35265538],
                                       [-0.54345106, 0.13113995],
                                       [-0.57181448, 0.13594725],
                                       [-0.33713329, 0.05095243],
                                       [-0.65741384, 0.477976],
                                       [-0.79986067, 0.41733195],
                                       [-0.73856328, 0.80699537],
                                       [-0.66489165, 0.1181712]])}

        temp = [test_input[k] for k in test_input]
        total_array = np.concatenate(temp)

        params = {
            'problem': {'name': 'svm_classification'},
            'algorithm': {
                'name': 'SVM'
            },
            'multiclass_extension': {'name': 'OneAgainstRest'}
        }

        algo_input = get_input_instance('SVMInput')
        algo_input.training_dataset = training_input
        algo_input.test_dataset = test_input
        algo_input.datapoints = total_array

        result = run_algorithm(params, algo_input)
        self.assertEqual(result['testing_accuracy'], 1.0)
        self.assertEqual(result['predicted_classes'],
                         ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
                          'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])

    def test_classical_multiclass_all_pairs(self):
        training_input = {'A': np.asarray([[0.6560706, 0.17605998],
                                           [0.25776033, 0.47628296],
                                           [0.79687342, 0.26933706],
                                           [0.39016555, -0.08469916],
                                           [0.3994399, 0.13601573],
                                           [0.26752049, -0.03978988],
                                           [0.24026485, 0.01953518],
                                           [0.49490503, 0.17239737],
                                           [0.70171827, 0.5323737],
                                           [0.43221576, 0.42357294],
                                           [0.62864856, 0.45504447],
                                           [0.6259567, 0.30917324],
                                           [0.58272403, 0.20760754],
                                           [0.3938784, 0.17184466],
                                           [0.14154948, 0.06201424],
                                           [0.80202323, 0.40582692],
                                           [0.46779595, 0.39946754],
                                           [0.57660199, 0.21821317],
                                           [0.51044761, 0.03699459],
                                           [0.8690704, 0.70847635]]),
                          'B': np.asarray([[0.38857596, -0.33775802],
                                           [0.49946978, -0.48727951],
                                           [-0.30119743, -0.11221681],
                                           [-0.16479252, -0.08640519],
                                           [-0.21808884, -0.56508327],
                                           [-0.14683258, -0.46528508],
                                           [-0.05888195, -0.51474852],
                                           [0.20517435, -0.66839091],
                                           [0.25475584, -0.21239966],
                                           [0.55194854, 0.02789679],
                                           [-0.11542951, -0.54157026],
                                           [0.44625538, -0.49485869],
                                           [-0.14609118, -0.60719757],
                                           [0.18121305, -0.1922198],
                                           [0.19283785, -0.31798925],
                                           [0.29626405, -0.54563098],
                                           [-0.39044304, -0.36527253],
                                           [-0.29432215, -0.43924164],
                                           [-0.40294517, -0.31381308],
                                           [0.49156185, -0.3660534]]),
                          'C': np.asarray([[-0.68088231, 0.46824423],
                                           [-0.56167659, 0.65270294],
                                           [-0.54323753, 0.67630888],
                                           [-0.57685569, -0.08515631],
                                           [-0.67765364, 0.19654347],
                                           [-0.62129115, 0.22223066],
                                           [-0.78040851, 0.65247848],
                                           [-0.50730279, 0.59898039],
                                           [-0.64275805, 0.63381998],
                                           [-0.72854201, 0.14151325],
                                           [-0.57004437, 0.12344874],
                                           [-0.55215973, 0.74331215],
                                           [-0.60916047, 0.52006917],
                                           [-0.23093745, 1.],
                                           [-0.84025337, 0.5564536],
                                           [-0.66952391, 0.57918859],
                                           [-0.67725082, 0.60439934],
                                           [-1., 0.23715261],
                                           [-0.62933025, 0.19055405],
                                           [-0.82139073, 0.29941512]])}

        test_input = {'A': np.asarray([[0.57483139, 0.47120732],
                                       [0.48372348, 0.25438544],
                                       [0.08791134, 0.11515506],
                                       [0.45988094, 0.32854319],
                                       [0.53015085, 0.41539212],
                                       [0.5073321, 0.47346751],
                                       [0.71081819, 0.19202569],
                                       [1., 0.51698289],
                                       [0.630973, 0.19898666],
                                       [0.48142649, 0.15931707]]),
                      'B': np.asarray([[-0.06048935, -0.48345293],
                                       [-0.01065613, -0.33910828],
                                       [-0.17323832, -0.49535592],
                                       [0.14043268, -0.87869109],
                                       [-0.15046837, -0.47340207],
                                       [-0.39600934, -0.21647957],
                                       [-0.394202, -0.44705385],
                                       [0.15243621, -0.36695163],
                                       [0.06195634, -0.23262325],
                                       [0.06183066, -0.53376975]]),
                      'C': np.asarray([[-0.74561108, 0.27047295],
                                       [-0.69942965, 0.11885162],
                                       [-0.52649891, 0.35265538],
                                       [-0.54345106, 0.13113995],
                                       [-0.57181448, 0.13594725],
                                       [-0.33713329, 0.05095243],
                                       [-0.65741384, 0.477976],
                                       [-0.79986067, 0.41733195],
                                       [-0.73856328, 0.80699537],
                                       [-0.66489165, 0.1181712]])}

        temp = [test_input[k] for k in test_input]
        total_array = np.concatenate(temp)

        params = {
            'problem': {'name': 'svm_classification'},
            'algorithm': {
                'name': 'SVM'
            },
            'multiclass_extension': {'name': 'AllPairs'}

        }

        algo_input = get_input_instance('SVMInput')
        algo_input.training_dataset = training_input
        algo_input.test_dataset = test_input
        algo_input.datapoints = total_array

        result = run_algorithm(params, algo_input)
        self.assertEqual(result['testing_accuracy'], 1.0)
        self.assertEqual(result['predicted_classes'],
                         ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B',
                          'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
                          'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])

    def test_classical_multiclass_error_correcting_code(self):
        training_input = {'A': np.asarray([[0.6560706, 0.17605998],
                                           [0.25776033, 0.47628296],
                                           [0.79687342, 0.26933706],
                                           [0.39016555, -0.08469916],
                                           [0.3994399, 0.13601573],
                                           [0.26752049, -0.03978988],
                                           [0.24026485, 0.01953518],
                                           [0.49490503, 0.17239737],
                                           [0.70171827, 0.5323737],
                                           [0.43221576, 0.42357294],
                                           [0.62864856, 0.45504447],
                                           [0.6259567, 0.30917324],
                                           [0.58272403, 0.20760754],
                                           [0.3938784, 0.17184466],
                                           [0.14154948, 0.06201424],
                                           [0.80202323, 0.40582692],
                                           [0.46779595, 0.39946754],
                                           [0.57660199, 0.21821317],
                                           [0.51044761, 0.03699459],
                                           [0.8690704, 0.70847635]]),
                          'B': np.asarray([[0.38857596, -0.33775802],
                                           [0.49946978, -0.48727951],
                                           [-0.30119743, -0.11221681],
                                           [-0.16479252, -0.08640519],
                                           [-0.21808884, -0.56508327],
                                           [-0.14683258, -0.46528508],
                                           [-0.05888195, -0.51474852],
                                           [0.20517435, -0.66839091],
                                           [0.25475584, -0.21239966],
                                           [0.55194854, 0.02789679],
                                           [-0.11542951, -0.54157026],
                                           [0.44625538, -0.49485869],
                                           [-0.14609118, -0.60719757],
                                           [0.18121305, -0.1922198],
                                           [0.19283785, -0.31798925],
                                           [0.29626405, -0.54563098],
                                           [-0.39044304, -0.36527253],
                                           [-0.29432215, -0.43924164],
                                           [-0.40294517, -0.31381308],
                                           [0.49156185, -0.3660534]]),
                          'C': np.asarray([[-0.68088231, 0.46824423],
                                           [-0.56167659, 0.65270294],
                                           [-0.54323753, 0.67630888],
                                           [-0.57685569, -0.08515631],
                                           [-0.67765364, 0.19654347],
                                           [-0.62129115, 0.22223066],
                                           [-0.78040851, 0.65247848],
                                           [-0.50730279, 0.59898039],
                                           [-0.64275805, 0.63381998],
                                           [-0.72854201, 0.14151325],
                                           [-0.57004437, 0.12344874],
                                           [-0.55215973, 0.74331215],
                                           [-0.60916047, 0.52006917],
                                           [-0.23093745, 1.],
                                           [-0.84025337, 0.5564536],
                                           [-0.66952391, 0.57918859],
                                           [-0.67725082, 0.60439934],
                                           [-1., 0.23715261],
                                           [-0.62933025, 0.19055405],
                                           [-0.82139073, 0.29941512]])}

        test_input = {'A': np.asarray([[0.57483139, 0.47120732],
                                       [0.48372348, 0.25438544],
                                       [0.08791134, 0.11515506],
                                       [0.45988094, 0.32854319],
                                       [0.53015085, 0.41539212],
                                       [0.5073321, 0.47346751],
                                       [0.71081819, 0.19202569],
                                       [1., 0.51698289],
                                       [0.630973, 0.19898666],
                                       [0.48142649, 0.15931707]]),
                      'B': np.asarray([[-0.06048935, -0.48345293],
                                       [-0.01065613, -0.33910828],
                                       [-0.17323832, -0.49535592],
                                       [0.14043268, -0.87869109],
                                       [-0.15046837, -0.47340207],
                                       [-0.39600934, -0.21647957],
                                       [-0.394202, -0.44705385],
                                       [0.15243621, -0.36695163],
                                       [0.06195634, -0.23262325],
                                       [0.06183066, -0.53376975]]),
                      'C': np.asarray([[-0.74561108, 0.27047295],
                                       [-0.69942965, 0.11885162],
                                       [-0.52649891, 0.35265538],
                                       [-0.54345106, 0.13113995],
                                       [-0.57181448, 0.13594725],
                                       [-0.33713329, 0.05095243],
                                       [-0.65741384, 0.477976],
                                       [-0.79986067, 0.41733195],
                                       [-0.73856328, 0.80699537],
                                       [-0.66489165, 0.1181712]])}

        temp = [test_input[k] for k in test_input]
        total_array = np.concatenate(temp)

        params = {
            'problem': {'name': 'svm_classification'},
            'algorithm': {
                'name': 'SVM',
            },
            'multiclass_extension': {'name': 'ErrorCorrectingCode', 'code_size': 5},
        }

        algo_input = get_input_instance('SVMInput')
        algo_input.training_dataset = training_input
        algo_input.test_dataset = test_input
        algo_input.datapoints = total_array

        result = run_algorithm(params, algo_input)
        self.assertEqual(result['testing_accuracy'], 1.0)
        self.assertEqual(result['predicted_classes'],
                         ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B',
                          'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
                          'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'])
