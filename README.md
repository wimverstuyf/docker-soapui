# Docker SoapUI

> Docker container that houses a configurable version of SoapUI and runs test suites


# Develop

> I use Vagrant to mimic the environment of Docker

```bash
$ vagrant up
$ vagrant ssh
# sudo -i
# cd /vagrant
# ./server.py
```

Once the server is up and running, you can now fire off SoapUI tests by sending the SoapUI project file  
Vagrant forwards the 3000 port to your local machine.

```sh
$ curl --form "data=@/users/ddavison/work/ericsson/soapui/soapui-project.xml" \
       --form "url=http://jsonplaceholder.typicode.com" \
       --form "suite=TestSuite" \
       http://localhost:3000
```

```
================================
=
= SOAPUI_HOME = /opt/SoapUI
=
================================
SoapUI 5.2.1 TestCase Runner
21:25:16,455 INFO  [SoapUITestCaseRunner] Running SoapUI tests in project [Something]
21:25:16,456 INFO  [SoapUITestCaseRunner] Running TestSuite [http://jsonplaceholder.typicode.com TestSuite], runType = SEQUENTIAL
21:25:16,463 INFO  [SoapUITestCaseRunner] Running SoapUI testcase [TestCase]
21:25:16,467 INFO  [SoapUITestCaseRunner] running step [Posts]
21:25:17,631 INFO  [SoapUITestCaseRunner] Assertion [XPath Match] has status VALID
21:25:17,634 INFO  [SoapUITestCaseRunner] Finished running SoapUI testcase [TestCase], time taken: 766ms, status: FINISHED
21:25:17,634 INFO  [SoapUITestCaseRunner] TestSuite [http://jsonplaceholder.typicode.com TestSuite] finished with status [FINISHED] in 1175ms
```
