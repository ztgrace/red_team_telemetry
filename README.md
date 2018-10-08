# Red Team Telemetry

A collection of scripts and configurations to enable centralized logging of red team infrastructure.

## What's in the repo?

* cobaltstrike
  * filebeat - filebeat configurations for cobalt strike
  * json_log.cna - An aggressor script to create a structured json log of beacon events
    * There's a known issue where this script will bomb out with a Java StackOverflow error if the logging directory doesn't exist. Be sure to run `mkdir /var/log/cobaltstrike` before you start the logger.
    * If there's an event type with no match, the event gets printed to the console and written to the ironically named `notlogged.log`.
    * Each log message is tagged with a role based on the username running the script. Example roles might be working, longhaul, test, dev, etc. The role is defined by grabbing the second array element when splitting the name by an underscore. For example, `logbot_test` would create a key:value pair of `"role":"test"` in the log entry.
    * The variables `$log_*` are used to enable/disable logging of those event types. Tweak these to your needs.
    * The `attack` hash map is generated using the `mitre_cs.py` script. As the ATT&CK Matrix gets updated this will need to be updated.
  * event_spy.cna - test script to print all events to the screen
  * mitre_cs.py - script to generate aggressor code for enriching tactic IDs with their phase
* packetbeat
  * packetbeat.yml - configuration for logging HTTP and DNS C2

## Blog Posts

* Red Team Telemetry Part 1 - https://zachgrace.com/posts/red-team-telemetry-part-1/

## Presentations

* DerbyCon 8
  * [DerbyCon 8 - Red Team Telemetry Slides.pdf](https://github.com/ztgrace/red_team_telemetry/blob/master/DerbyCon_8_-_Red_Team_Telemetry_Slides.pdf)
  * https://www.irongeek.com/i.php?page=videos/derbycon8/track-2-14-red-mirror-bringing-telemetry-to-red-teaming-zach-grace

## Similar Research

* CobaltSplunk
  * https://vincentyiu.co.uk/cobaltsplunk/
  * https://github.com/vysec/CobaltSplunk
* RedELK
  * https://github.com/outflanknl/RedELK
  * https://www.youtube.com/watch?v=cwJNaWrOolk
* RedTeamSIEM
  * https://github.com/SecurityRiskAdvisors/RedTeamSIEM
  * https://www.youtube.com/watch?v=xH1TeVtG1M8&feature=youtu.be
