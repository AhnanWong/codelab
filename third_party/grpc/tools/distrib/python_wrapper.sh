#!/bin/sh

# Copyright 2016 gRPC authors.
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

for p in python2.7 python2.6 python2 python not_found ; do 

  python=$(which $p || echo not_found)

  if [ -x "$python" ] ; then
    break
  fi

done

if [ -x "$python" ] ; then
  exec "$python" "$@"
else
  echo "No acceptable version of python found on the system"
  exit 1
fi
