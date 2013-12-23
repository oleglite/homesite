function getRandomColor(minColor, maxColor) {
    if (minColor === undefined) {
        minColor = 0;
    }
    if (maxColor === undefined) {
        maxColor = 0xffffff;
    }
    return '#' + (0x1000000 + minColor + (Math.random()) * (maxColor - minColor)).toString(16).substr(1, 6)
}

function showChart(canvasId, sections) {
    var ctx = $("#" + canvasId).get(0).getContext("2d");

    for (i = 0; i < sections.length; i++) {
        section = sections[i];
        if (!section.color) {
            section.color = getRandomColor(0, 0xeeeeee);
        }
    }

    var myPie = new Chart(ctx).Pie(sections, null);
}

function showSkillCharts() {
    var chartBlocks = $(".detailed_content").find('.skill_chart_block');
    for (var i = 0; i < chartBlocks.length; i++) {
        var chartBlock = $(chartBlocks[i]);
        var canvasId = $(chartBlock.find('.skill_chart')[0]).attr('id');
        var chartSectionsData = $(chartBlock.find('.chart_data'));

        var sections = [];
        for (var j = 0; j < chartSectionsData.length; j++) {
            data = $(chartSectionsData[j]).data();
            sections.push({
                'value': data['value'],
                'label': data['label'],
                'labelColor': data['labelcolor'],
                'labelFontSize': data['labelfontsize'].toString()
            });
        }
        var justScope = function (canvasId, sections, delay) {
            chartBlock.delay(delay).fadeIn(600, function() {
                showChart(canvasId, sections);
            });
        }(canvasId, sections, i * 700);
    }
}

function showSkillDetails() {
    $('.detailed_button').slideUp();
    $('.detailed_content').slideDown(400, showSkillCharts);
}

$(document).ready(function () {
    $('#skills_detailed_button').click(showSkillDetails);
});