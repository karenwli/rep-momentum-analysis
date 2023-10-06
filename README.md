# rep-momentum-analysis
Comprehensive overview of work on the memory momentum project

## Memory Momentum Project: A guide to this zip file

### File Structure
-	Norming- Results of norming study, also previous linguistic stimuli we discussed
-	Experiment 1 (SONA)- Results of Exp1 as run on SONA, also experiment code and R analysis files
-	Experiment 1 (Prolific)- Results of Exp2 as run on Prolific, also experiment code and R analysis files
-	Experiment 2- Results of Exp2 as run on Prolific, also experiment code and R analysis files
-	Literature and writeup- Some slides from update meetings, also a more comprehensive writeup. 
-	Stimuli- A list of stimuli, the original images and videos, and a python script to resize the images and make them into videos.

### State of the project:

There is a proven effect, representational momentum, that even without linguistic input, people will mentally progress an telic event past the cutoff point that they have actually seen. This project attempts to study the effect of linguistic input (in the form of goals) on how a person stores events in their memory. Will a more ambitious goal push their memory state further towards completion, or will a more conservative goal further encourage mental completion of the event?

So far, we’ve run a norming study and two experiments, the first of which is a forced choice between two incorrect options, and shows forward momentum in the condition of no goals and low goals, but no significant momentum in the condition of high goals. Experiment 2 offers the correct frame (as well as all other frames), and shows that people have no pattern of forward error when shown no goal and offered the correct choice. There is a greater pattern of forward error when shown a goal (high or low), but as of right now the results are not significant. As it stands, Experiments 1 and 2 are in slight conflict, since Experiment 1 indicates a baseline level of forward error, and Experiment 2 does not. 

### Moving forward:

Before conducting analyses, I recommend redownloading the data from the PCIbex backend:
-	karen_memory_exp1_nogoals
-	karen_memory_exp1_highlow
-	karen_memory_exp2_slider
Moving forward, there are a few directions. First is to clear up the contradiction in the results between Experiments 1 and 2. Then, we can consider different variations upon the original experiment. 


#### Troubleshooting Experiments 1 and 2:
Option 1: The results are accurate, and there is some way to reconcile these two experiments under one theory

Option 2: Error has been introduced through the stimuli by use of inconsistent event types, goal calibrations, or something similar

Option 3: Error has been introduced through the experimental design-- participants were not required to move the randomized slider before continuing, so this might reflect some of those unaltered responses. (Note: randomized slider was to reduce bias towards beginning of event) Retroactively eliminating this data would likely involve filtering reaction times based on the last item logged in PCIbex. Preventing this in the future would require editing the video_scrubber element in PCIbex to prevent a participant from continuing if they have not moved the slider (I would ask June how to do that)

#### Variations upon the original experiment:

-	Negative goals: As suggested by Alon Hafri, we might consider “negative goals” that encourage as little perceived change in the event as possible. Negative goals for the existing stimuli were tested in the norming study and should be ready to go
-	Static stimuli: Instead of showing a stop motion animation, simply show the final frame and test the representational momentum elicited. This is less likely to show a strong effect, but has precedent in early representational momentum studies (think freeze frame of dog jumping into water)
-	Arrow input: Instead of clicking the slider to select a frame, the participant would have to use their arrow keys to progress through the frames before settling on one. This forces the participant to essentially replay the clip from start to end, rather than skipping directly to the last moment they remember. This was suggested by June Choe, and the PCIbex mockup is in the zip file “karen_memory_exp4_arrowkey”

If creating new stimuli, the thought process behind the critical items was that one event was a subset of the other, and the thought process behind the fillers was that they were two events that were indistinguishable until the 50% mark. 


