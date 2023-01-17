# Copyright 2023 Dragan Filipovic

# Based on https://gist.github.com/nyurik/d438cb56a9059a0660ce4176ef94576f

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup

setup(
    name='physical2logical',

    version='1.0.1',

    description='Convert CSS physical properties to logical',
    long_description='Converts margins, padding, and borders to logical values, allowing RTL and vertical languages '
                     'to show correctly.',
    long_description_content_type='text/x-rst',

    author='Dragan Filipovic / Yuri Astrakhan',
    author_email='info@frontenddot.com',

    license='Apache Software License',

    packages=['physical2logical'],
    zip_safe=False,
)
