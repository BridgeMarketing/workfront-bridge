import mock
import unittest

from workfront_bridge.blocks import base


class BaseBuilderTest(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.object(base.WFBlockParser, 'create')
        self.addCleanup(patcher.stop)
        create = patcher.start()
        create.side_effect = self.mock_parser_create

    def mock_parser_create(self, block):
        parsed = {
            task: params
            for task, params in block.parameters.iteritems()
        }
        parsed['wf_template_name'] = block.wf_template_name
        if block.blocks:
            parsed['blocks'] = [self.mock_parser_create(sub) for sub in block.blocks]
        return parsed

    def assertDeepEquals(self, expected, actual, path=''):
        self.assertIsInstance(expected, (dict, list), 'unsupported type {} at {}'.format(
            type(expected), path,
        ))

        if isinstance(expected, dict):
            self.assertIsInstance(actual, dict, 'expecting dict but found {} at {}'.format(
                type(actual), path,
            ))

            expected_keys = tuple(sorted(expected.keys()))
            actual_keys = tuple(sorted(actual.keys()))

            self.assertItemsEqual(
                expected_keys,
                actual_keys,
                'Different key set at {} expected({}) found({})'.format(
                    path, ','.join(expected_keys), ','.join(actual_keys),
                )
            )

            for k, v in expected.iteritems():
                self.assertIsInstance(k, basestring, 'key is not a string {}/{}'.format(path, k))
                self.assertIsInstance(v, (basestring, dict, list), 'unsupported type {} at {}/{}'.format(
                    type(v), path, k,
                ))

                if isinstance(v, basestring):
                    self.assertEquals(
                        v,
                        actual[k],
                        'different values at {}/{} expected "{}" but found "{}"'.format(
                            path, k, v, actual[k],
                        )
                    )
                #elif isinstance(v, (list, dict)):
                    #self.assertDeepEquals(v, actual[k], path + '/' + k)
        elif isinstance(expected, list):
            self.assertEquals(len(expected), len(actual), 'different number of items at {}'.format(path))

            for i, v in enumerate(expected):
                self.assertIsInstance(v, (basestring, dict, list), 'unsupported type {} at {}[{}]'.format(
                    type(v), path, i,
                ))

                if isinstance(v, basestring):
                    self.assertEquals(
                        v,
                        actual[i],
                        'different values at {}[{}] expected "{}" but found "{}"'.format(
                            path, i, v, actual[i],
                        )
                    )
                elif isinstance(v, (list, dict)):
                    self.assertDeepEquals(v, actual[i], '{}[{}]'.format(path, i))
