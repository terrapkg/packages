let html = req("https://groovy.apache.org/download.html");
rpm.version(find(`onclick='window\\.location\\.href="https://groovy.jfrog.io/artifactory/dist-release-local/groovy-zips/apache-groovy-sdk-([\\d.]+)\\.zip"'>`, html, 1));
