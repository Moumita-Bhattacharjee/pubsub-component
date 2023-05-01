#!/bin/bash

aws s3 cp ./pubsub.zip "s3://care-cam/artifacts/com.t2s.pubsub/$1/pubsub.zip"
