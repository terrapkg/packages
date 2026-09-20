#!/bin/sh

exec /usr/bin/java \
    -Xmx512m \
    -Djava.locale.providers=COMPAT \
    --module-path /usr/share/openjfx/lib \
    --add-modules=javafx.controls,javafx.swing,javafx.media,javafx.web,java.instrument,jdk.attach \
    --add-exports javafx.graphics/com.sun.javafx.iio=ALL-UNNAMED \
    --add-exports javafx.graphics/com.sun.javafx.iio.common=ALL-UNNAMED \
    --add-exports javafx.graphics/com.sun.javafx.scene.text=ALL-UNNAMED \
    --add-exports javafx.graphics/com.sun.javafx.geom=ALL-UNNAMED \
    --add-exports javafx.graphics/com.sun.javafx.tk=ALL-UNNAMED \
    --add-exports javafx.web/com.sun.javafx.webkit=ALL-UNNAMED \
    --add-exports javafx.web/com.sun.webkit=ALL-UNNAMED \
    --add-opens javafx.graphics/javafx.scene.text=ALL-UNNAMED \
    --add-opens javafx.graphics/com.sun.javafx.text=ALL-UNNAMED \
    -cp '/usr/share/java/quollwriter/*' \
    com.quollwriter.Startup "$@"
