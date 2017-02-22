# Copyright 2012 Hewlett-Packard Development Company, L.P.
# Copyright 2012 Varnish Software AS
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""
Builders define actions that the Jenkins job should execute.  Examples
include shell scripts or maven targets.  The ``builders`` attribute in
the :ref:`Job` definition accepts a list of builders to invoke.  They
may be components defined below, locally defined macros (using the top
level definition of ``builder:``, or locally defined components found
via the ``jenkins_jobs.builders`` entry point.

**Component**: builders
  :Macro: builder
  :Entry Point: jenkins_jobs.builders

Example::

  job:
    name: test_job

    builders:
      - shell: "make test"

"""

import logging
import xml.etree.ElementTree as XML

from jenkins_jobs.errors import InvalidAttributeError
from jenkins_jobs.errors import JenkinsJobsException
from jenkins_jobs.errors import MissingAttributeError
import jenkins_jobs.modules.base
from jenkins_jobs.modules.helpers import append_git_revision_config
import pkg_resources
from jenkins_jobs.modules.helpers import cloudformation_init
from jenkins_jobs.modules.helpers import cloudformation_region_dict
from jenkins_jobs.modules.helpers import cloudformation_stack
from jenkins_jobs.modules.helpers import config_file_provider_builder
from jenkins_jobs.modules.helpers import config_file_provider_settings
from jenkins_jobs.modules.helpers import convert_mapping_to_xml
from jenkins_jobs.modules.helpers import copyartifact_build_selector
from jenkins_jobs.modules import hudson_model

logger = logging.getLogger(__name__)

def ScalrJenkins(parser, xml_parent, data):
    """
	yaml: builders
	
**Component**: builders
  :Macro: builder
  :Entry Point: jenkins_jobs.builders
    
    Example::

      builders:
      - ScalrJenkins:
          deployToAllServers: 'false'
          deployUsingyaml: 'false'
          deployToParticularServer: 'true'
          deploymenttype: 'DeployToParticularServer'
          env__Id__Server: '1'
          farmName__Server: 'demo instances'
          ServerID__Server: 'f99e54ab-31ad-417a-99ac-66bde3c6576c'
          artifactUrl__Server: 'http://nexus/artifact/test.html'
          scriptId__Server: '9'
          yamlFileName: ''
          env__Id__All__servers: ''
          farmName__All__servers: ''
          artifactUrl__All__servers: ''
          scriptId__All__servers: ''
    """
    #logger = logging.getLogger("%s:ScalrJenkins" % __name__)
    ScalrJenkins = XML.SubElement(xml_parent, 'com.hpi.ScalrJenkins.ScalrJenkins')   
    print(data)
    XML.SubElement(ScalrJenkins, 'env__Id__Server').text = data['env__Id__Server']
    XML.SubElement(ScalrJenkins, 'farmName__Server').text = data['farmName__Server']
    XML.SubElement(ScalrJenkins, 'ServerID__Server').text = data['ServerID__Server']
    XML.SubElement(ScalrJenkins, 'artifactUrl__Server').text = data['artifactUrl__Server']
    XML.SubElement(ScalrJenkins, 'scriptId__Server').text = data['scriptId__Server']
    XML.SubElement(ScalrJenkins, 'env__Id__All__servers').text = data['env__Id__All__servers']
    XML.SubElement(ScalrJenkins, 'farmName__All__servers').text = data['farmName__All__servers']
    XML.SubElement(ScalrJenkins, 'artifactUrl__All__servers').text = data['artifactUrl__All__servers']
    XML.SubElement(ScalrJenkins, 'scriptId__All__servers').text = data['scriptId__All__servers']
    XML.SubElement(ScalrJenkins, 'deploymenttype').text = data['deploymenttype']
    XML.SubElement(ScalrJenkins, 'deployToAllServers').text = data['deployToAllServers']
    XML.SubElement(ScalrJenkins, 'deployUsingyaml').text = data['deployUsingyaml']
    XML.SubElement(ScalrJenkins, 'deployToParticularServer').text = data['deployToParticularServer']
    XML.SubElement(ScalrJenkins, 'yamlFileName').text = data['yamlFileName']
