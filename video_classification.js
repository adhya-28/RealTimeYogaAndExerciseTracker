var pose;

const set1_labels_info = { 0: "dog", 1: "tree", 2: "warrior1" };
const set2_labels_info = { 0: "goddess", 1: "mountain", 2: "warrior2" };
//variables coming from web_classification

function changeData() {
  // Retrieve yoga set from sessionStorage
    const yogaSet = sessionStorage.getItem("yogaSet");
    if (yogaSet === "1") {
        // Randomly select a pose from set 1
        pose = set1_labels_info[Math.floor(Math.random() * Object.keys(set1_labels_info).length)];
    } else if (yogaSet === "2") {
        // Randomly select a pose from set 2
        pose = set2_labels_info[Math.floor(Math.random() * Object.keys(set2_labels_info).length)];
    }


    const advDisAdv = {
        dog: {
            adv: ["Tones the arms and legs; opens and strengthens the shoulders in flexion", "lengthens the hamstrings and stretches the calves", "prepares the body for heating inversion"],
            disAdv: [" Be careful if there is an existing wrist or shoulder injury", "high blood pressure or headache should modify with support for the head (bolster or blankets)", "late-term pregnancy"]
        },
        tree: {
            adv: ["physical and mental steadiness", "Tree Pose improves focus and concentration while calming your mind.", "Tree Pose stretches the thighs, groins, torso, and shoulders. It builds strength in the ankles and calves, and tones the abdominal muscles"],
            disAdv: ["experiencing headaches, insomnia, low blood pressure, or if you are lightheaded and/or dizzy.Those with high blood pressure should not raise their arms overhead in the pose"]
        },
        mountain: {
            adv: ["Abdomen, back, legs", "prepares the body for heat extraction"],
            disAdv: [" Be careful if there is an existing wrist or shoulder injury"]
        },
        warrior1: {
            adv: [" Stretches the chest and lungs, shoulders and neck, belly, groins (psoas)", "Strengthens the shoulders and arms, and the muscles of the back", "Strengthens and stretches the thighs, calves, and ankles"],
            disAdv: [" High blood pressure", "Heart problems", "Students with shoulder problems should keep their raised arms parallel (or slightly wider than parallel) to each other", "Students with neck problems should keep their heads in a neutral position and not look up at the hands."]
        },
        warrior2: {
            adv: ["Strengthens and stretches the legs and ankles", "Stretches the groins, chest and lungs, shoulders", "Stimulates abdominal organs", "Increases stamina", "Relieves backaches, especially through the second trimester of pregnancy", "Therapeutic for carpal tunnel syndrome, flat feet, infertility, osteoporosis, and sciatica"],
            disAdv: ["Diarrhea", " High blood pressure", "Neck problems", "Don’t turn your head to look over the front hand"]
        },
        goddess: {
            adv: [" major hip-opening, lower back, hamstrings, knees, pelvic, quadriceps benefits", "recommended during pregnancy", "help improve balance, focus, and concentration,"],
            disAdv: [" Be careful if there is an existing wrist or shoulder injury", "high blood pressure or headache should modify with support for the head (bolster or blankets)", "late-term pregnancy"]
        }
    }
    // gif.src = `./static/tutorials/${pose}.gif`;
    // gifName.innerText = `${getPoseDisplayName(pose)} Pose`;
    
    document.getElementById("gif").src = `./static/tutorials/${pose}.gif`;
    document.getElementById("gifname").innerText = `${getPoseDisplayName(pose)} Pose`;
    let advantages = advDisAdv[pose].adv;
    let advs = "";
    advantages.forEach(item => advs += item + "<br>");
    document.getElementById("adv").innerHTML = advs;

    let disAdvantages = advDisAdv[pose].disAdv;
    let disAd = "";
    disAdvantages.forEach(item => disAd += item + "<br>");
    document.getElementById("disAdv").innerHTML = disAd;
}


function getPoseDisplayName(pose) {
    switch (pose) {
        case 'dog':
            return 'Downward-Dog';
        case 'tree':
            return 'Tree';
        case 'mountain':
            return 'Mountain';
        case 'warrior1':
            return 'Warrior1';
        case 'warrior2':
            return 'Warrior2';
        case 'goddess':
            return 'Goddess';
        default:
            return pose;
    }
}
document.addEventListener('DOMContentLoaded', () => {
    setInterval(changeData, 6000); // Call changeData every second for demo
});

// TODOO:New feature time pose
var sec = 0;
var min = 0;
var stopStatus = false;

var x;
const startTimer = () => {
    x = setInterval(function () {
        sec++;
        $('.timer').text(min + ' : ' + sec);
        if (stopStatus === false) {
            if (sec === 59) {
                sec = -1;
                min++;

            }
        } else {
            clearInterval(x);
            startTimer();
        }
    }, 1000);
}

const stopTimer = () => {
    console.log("stop timer");
    stopStatus = true;
    clearInterval(x);
}

const resetTimer = () => {
    console.log("reset timer");
    let posex = pose;
    let time = min + " : " + sec;
    if (sessionStorage.getItem("excerciseDuration") === null) {

        var arr = new Array();
        let s = {};
        s[posex] = time;
        arr[0] = s;
        for (let i = 0; i < arr.length; i++) {
            arr[i] = JSON.stringify(arr[i]);
        }

        arr = JSON.stringify(arr);

        //save to session storage
        sessionStorage.setItem('excerciseDuration', arr);
        var y = sessionStorage.getItem('excerciseDuration');
        y = JSON.parse(y);
        y.forEach((item, index) => {
            y[index] = JSON.parse(item);
        });
        // location.reload();

    } else {
        var y = sessionStorage.getItem('excerciseDuration');
        y = JSON.parse(y);
        y.forEach((item, index) => {
            y[index] = JSON.parse(item);
        });
        console.log(posex);

        let s = {};
        s[posex] = time;
        y.push(s);

        for (let i = 0; i < y.length; i++) {
            y[i] = JSON.stringify(y[i]);
        }
        y = JSON.stringify(y);

        //save to session storage
        sessionStorage.setItem('excerciseDuration', y);
        // location.reload();
    }
    stopStatus = true;
    clearInterval(x);
    sec = 0;
    min = 0;
    $('.timer').text(min + ' : ' + sec);
}

// Load table data (you can implement this function)
function loadTableData() {
    const exerciseDuration = sessionStorage.getItem('excerciseDuration');
    if (exerciseDuration) {
        const durationArray = JSON.parse(exerciseDuration);
        const tableBody = document.querySelector('.table tbody');
        tableBody.innerHTML = ''; // Clear existing rows

        durationArray.forEach(item => {
            const pose = Object.keys(item)[0];
            const duration = Object.values(item)[0];
            tableBody.innerHTML += `<tr><td>${pose}</td><td>${duration}</td></tr>`;
        });
    }
}

// Call necessary functions on page load
// window.onload = function () {
//     yoga_set = sessionStorage.getItem("yogaSet");
//     initialize(yoga_set)
//     loadmodel();
   
//     loadTableData(); // Call this function to populate the table

// };

// const changeData = (pred_index) => {
//     // pred_index = 2;
//     console.log(pred_index);

//     const advDisAdv = {
//         dog: {
//             adv: ["Tones the arms and legs; opens and strengthens the shoulders in flexion", "lengthens the hamstrings and stretches the calves", "prepares the body for heating inversion"],
//             disAdv: [" Be careful if there is an existing wrist or shoulder injury", "high blood pressure or headache should modify with support for the head (bolster or blankets)", "late-term pregnancy"]
//         },
//         tree: {
//             adv: ["physical and mental steadiness", "Tree Pose improves focus and concentration while calming your mind.", "Tree Pose stretches the thighs, groins, torso, and shoulders. It builds strength in the ankles and calves, and tones the abdominal muscles"],
//             disAdv: ["experiencing headaches, insomnia, low blood pressure, or if you are lightheaded and/or dizzy.Those with high blood pressure should not raise their arms overhead in the pose"]
//         },
//         mountain: {
//             adv: ["Abdomen, back, legs", "prepares the body for heat extraction"],
//             disAdv: [" Be careful if there is an existing wrist or shoulder injury"]
//         },
//         warrior1: {
//             adv: [" Stretches the chest and lungs, shoulders and neck, belly, groins (psoas)", "Strengthens the shoulders and arms, and the muscles of the back", "Strengthens and stretches the thighs, calves, and ankles"],
//             disAdv: [" High blood pressure", "Heart problems", "Students with shoulder problems should keep their raised arms parallel (or slightly wider than parallel) to each other", "Students with neck problems should keep their heads in a neutral position and not look up at the hands."]
//         },
//         warrior2: {
//             adv: ["Strengthens and stretches the legs and ankles", "Stretches the groins, chest and lungs, shoulders", "Stimulates abdominal organs", "Increases stamina", "Relieves backaches, especially through the second trimester of pregnancy", "Therapeutic for carpal tunnel syndrome, flat feet, infertility, osteoporosis, and sciatica"],
//             disAdv: ["Diarrhea", " High blood pressure", "Neck problems", "Don’t turn your head to look over the front hand"]
//         },
//         goddess: {
//             adv: [" major hip-opening, lower back, hamstrings, knees, pelvic, quadriceps benefits", "recommended during pregnancy", "help improve balance, focus, and concentration,"],
//             disAdv: [" Be careful if there is an existing wrist or shoulder injury", "high blood pressure or headache should modify with support for the head (bolster or blankets)", "late-term pregnancy"]
//         }
//     }

//     const set1_labels_info = { 0: "dog", 1: "tree", 2: "warrior1" }
//     const set2_labels_info = { 0: "goddess", 1: "mountain", 2: "warrior2" }

//     yoga_set = sessionStorage.getItem("yogaSet");

//     if (yoga_set === "1") {
//         pose = set1_labels_info[pred_index]
//     } else if (yoga_set === "2") {
//         pose = set2_labels_info[pred_index]
//     }

//     document.getElementById("gif").src = './static/tutorials/' + pose + '.gif';
//     if(pose=="dog"){
//         document.getElementById("gifname").innerHTML = "Downward-Dog Pose";
//     }
//     if(pose=="tree"){
//         document.getElementById("gifname").innerHTML = "Tree Pose";
//     }
//     if(pose=="mountain"){
//         document.getElementById("gifname").innerHTML = "Mountain Pose";
//     }
//     if(pose=="warrior1"){
//         document.getElementById("gifname").innerHTML = "Warrior1 Pose";
//     }
//     if(pose=="warrior2"){
//         document.getElementById("gifname").innerHTML = "Warrio2 Pose";
//     }
//     if(pose=="goddess"){
//         document.getElementById("gifname").innerHTML = "Goddess Pose";
//     }

//     // document.getElementById('pose').innerHTML = pose;

//     if (pose === "dog") {
//         let advantages = advDisAdv.dog.adv;
//         var advs = "";
//         advantages.forEach((item, index) => {
//             advs += item + " " + "<br>";
//         })
//         document.getElementById("adv").innerHTML = advs;

//         let disAdvantages = advDisAdv.dog.disAdv;
//         var disAd = "";
//         disAdvantages.forEach((item, index) => {
//             disAd += item + " " + "<br>";
//         })
//         document.getElementById("disAdv").innerHTML = disAd;
//     } else if (pose === "tree") {
//         let advantages = advDisAdv.tree.adv;
//         var advs = "";
//         advantages.forEach((item, index) => {
//             advs += item + " " + "<br>";
//         })
//         document.getElementById("adv").innerHTML = advs;

//         let disAdvantages = advDisAdv.tree.disAdv;
//         var disAd = "";
//         disAdvantages.forEach((item, index) => {
//             disAd += item + " " + "<br>";
//         })
//         document.getElementById("disAdv").innerHTML = disAd;

//     } else if (pose === "mountain") {
//         let advantages = advDisAdv.mountain.adv;
//         var advs = "";
//         advantages.forEach((item, index) => {
//             advs += item + " " + "<br>";
//         })
//         document.getElementById("adv").innerHTML = advs;

//         let disAdvantages = advDisAdv.mountain.disAdv;
//         var disAd = "";
//         disAdvantages.forEach((item, index) => {
//             disAd += item + " " + "<br>";
//         })
//         document.getElementById("disAdv").innerHTML = disAd;

//     } else if (pose === "warrior1") {
//         let advantages = advDisAdv.warrior1.adv;
//         var advs = "";
//         advantages.forEach((item, index) => {
//             advs += item + " " + "<br>";
//         })
//         document.getElementById("adv").innerHTML = advs;

//         let disAdvantages = advDisAdv.warrior1.disAdv;
//         var disAd = "";
//         disAdvantages.forEach((item, index) => {
//             disAd += item + " " + "<br>";
//         })
//         document.getElementById("disAdv").innerHTML = disAd;

//     } else if (pose === "warrior2") {
//         let advantages = advDisAdv.warrior2.adv;
//         var advs = "";
//         advantages.forEach((item, index) => {
//             advs += item + " " + "<br>";
//         })
//         document.getElementById("adv").innerHTML = advs;

//         let disAdvantages = advDisAdv.warrior2.disAdv;
//         var disAd = "";
//         disAdvantages.forEach((item, index) => {
//             disAd += item + " " + "<br>";
//         })
//         document.getElementById("disAdv").innerHTML = disAd;

//     } else if (pose === "goddess") {
//         let advantages = advDisAdv.goddess.adv;
//         var advs = "";
//         advantages.forEach((item, index) => {
//             advs += item + " " + "<br>";
//         })
//         document.getElementById("adv").innerHTML = advs;

//         let disAdvantages = advDisAdv.goddess.disAdv;
//         var disAd = "";
//         disAdvantages.forEach((item, index) => {
//             disAd += item + " " + "<br>";
//         })
//         document.getElementById("disAdv").innerHTML = disAd;
//     }
// }