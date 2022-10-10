import { 
    ApexStrokeDefault, 
    ApexChartDefault,
    ApexColorDefault,
    ApexDataLabelDefault,
    ApexBarDefault,
    COLOR_1,
    COLOR_2,
    COLOR_3,
    COLOR_4
} from '../constant/chart.constant';

class Chart {

    static init() {
        const basicOptions = {
            series: [
                {
                    name: "Desktops",
                    data: [10, 41, 35, 51, 49, 62, 69, 91, 148],
                    color: COLOR_1
                }
            ],
            chart: {
                ...ApexChartDefault,
                height: 350,
                type: "line",
                zoom: {
                    enabled: false
                }
            },
            dataLabels: {
                enabled: false
            },
            stroke: ApexStrokeDefault,
            title: {
                text: "Product Trends by Month",
                align: "left"
            },
            grid: {
                row: {
                colors: ["#f3f3f3", "transparent"],
                    opacity: 0.5
                }
            },
            xaxis: {
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep"
                ]
            }
        };
        new ApexCharts(document.querySelector("#basic-chart"), basicOptions).render();

        const dashLineOption = {
            series: [
                {
                    name: "Session Duration",
                    data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10]
                },
                {
                    name: "Page Views",
                    data: [35, 41, 62, 42, 13, 18, 29, 37, 36, 51, 32, 35]
                },
                {
                    name: "Total Visits",
                    data: [87, 57, 74, 99, 75, 38, 62, 47, 82, 56, 45, 47]
                }
            ],
            chart: {
                ...ApexChartDefault,
                height: 350,
                type: "line"
            },
            dataLabels: ApexDataLabelDefault,
            stroke: {
                ...ApexStrokeDefault,
                dashArray: [0, 8, 5]
            },
            title: {
                text: "Page Statistics",
                align: "left"
            },
            color: ApexColorDefault,
            legend: {
                tooltipHoverFormatter: function(val, opts) {
                    return (
                        val +
                        " - <strong>" +
                        opts.w.globals.series[opts.seriesIndex][opts.dataPointIndex] +
                        "</strong>"
                    );
                }
            },
            markers: {
                size: 0,
                hover: {
                    sizeOffset: 6
                }
            },
            xaxis: {
                labels: {
                    trim: false
                },
                categories: [
                    "01 Jan",
                    "02 Jan",
                    "03 Jan",
                    "04 Jan",
                    "05 Jan",
                    "06 Jan",
                    "07 Jan",
                    "08 Jan",
                    "09 Jan",
                    "10 Jan",
                    "11 Jan",
                    "12 Jan"
                ]
            },
            tooltip: {
                y: [
                    {
                    title: {
                        formatter: function(val) {
                            return val + " (mins)";
                        }
                    }
                    },
                    {
                    title: {
                        formatter: function(val) {
                            return val + " per session";
                        }
                    }
                    },
                    {
                    title: {
                        formatter: function(val) {
                            return val;
                        }
                    }
                    }
                ]
            }
        }
        new ApexCharts(document.querySelector("#dashline-chart"), dashLineOption).render();

        const basicAreaOption = {
            series: [
                {
                    name: "STOCK ABC",
                    data: [
                        8107.85,
                        8128.0,
                        8122.9,
                        8165.5,
                        8340.7,
                        8423.7,
                        8423.5,
                        8514.3,
                        8481.85,
                        8487.7,
                        8506.9,
                        8626.2,
                        8668.95,
                        8602.3,
                        8607.55,
                        8512.9,
                        8496.25,
                        8600.65,
                        8881.1,
                        9340.85
                    ],
                    color: COLOR_1
                }
            ],
            chart: {
                ...ApexChartDefault,
                type: "area",
                height: 350,
                zoom: {
                    enabled: false
                }
            },
            dataLabels: ApexDataLabelDefault,
            title: {
                text: "Fundamental Analysis of Stocks",
                align: "left"
            },
            subtitle: {
                text: "Price Movements",
                align: "left"
            },
            labels: [
                "13 Nov 2017",
                "14 Nov 2017",
                "15 Nov 2017",
                "16 Nov 2017",
                "17 Nov 2017",
                "20 Nov 2017",
                "21 Nov 2017",
                "22 Nov 2017",
                "23 Nov 2017",
                "24 Nov 2017",
                "27 Nov 2017",
                "28 Nov 2017",
                "29 Nov 2017",
                "30 Nov 2017",
                "01 Dec 2017",
                "04 Dec 2017",
                "05 Dec 2017",
                "06 Dec 2017",
                "07 Dec 2017",
                "08 Dec 2017"
            ],
            xaxis: {
                type: "datetime"
            },
            yaxis: {
                opposite: true
            },
            legend: {
                horizontalAlign: "left"
            },
            stroke: ApexStrokeDefault
        }
        new ApexCharts(document.querySelector("#basic-area-chart"), basicAreaOption).render();

        const splineChartOption = {
            series: [
                {
                    name: "series1",
                    data: [31, 40, 28, 51, 42, 109, 100],
                    color: COLOR_1
                },
                {
                    name: "series2",
                    data: [11, 32, 45, 32, 34, 52, 41],
                    color: COLOR_2
                }
            ],
            chart: {
                ...ApexChartDefault,
                height: 350,
                type: "area"
            },
            dataLabels: ApexDataLabelDefault,
            stroke: ApexStrokeDefault,
            xaxis: {
                type: "datetime",
                categories: [
                    "2018-09-19T00:00:00.000Z",
                    "2018-09-19T01:30:00.000Z",
                    "2018-09-19T02:30:00.000Z",
                    "2018-09-19T03:30:00.000Z",
                    "2018-09-19T04:30:00.000Z",
                    "2018-09-19T05:30:00.000Z",
                    "2018-09-19T06:30:00.000Z"
                ]
            },
            tooltip: {
                x: {
                    format: "dd/MM/yy HH:mm"
                }
            }
        }
        new ApexCharts(document.querySelector("#spline-area-chart"), splineChartOption).render();

        const basicColumnOption = {
            series: [
                {
                    name: "Net Profit",
                    data: [44, 55, 57, 56, 61, 58, 63, 60, 66],
                    color: COLOR_1
                },
                {
                    name: "Revenue",
                    data: [76, 85, 101, 98, 87, 105, 91, 114, 94],
                    color: COLOR_2
                },
                {
                    name: "Free Cash Flow",
                    data: [35, 41, 36, 26, 45, 48, 52, 53, 41],
                    color: COLOR_3
                }
            ],
            chart: {
                ...ApexChartDefault,
                type: "bar",
                height: 350
            },
            plotOptions: ApexBarDefault,
            dataLabels: ApexDataLabelDefault,
            stroke: {
                show: true,
                width: 2,
                colors: ["transparent"]
            },
            xaxis: {
                categories: [
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct"
                ]
            },
            yaxis: {
                title: {
                    text: "$ (thousands)"
                }
            },
            fill: {
                opacity: 1
            },
            tooltip: {
                y: {
                    formatter: function(val) {
                        return "$ " + val + " thousands";
                    }
                }
            }
        }
        new ApexCharts(document.querySelector("#basic-column-chart"), basicColumnOption).render();

        const stackColumnOption = {
            series: [
                {
                    name: "PRODUCT A",
                    data: [44, 55, 41, 67, 22, 43],
                    color: COLOR_1
                },
                {
                    name: "PRODUCT B",
                    data: [13, 23, 20, 8, 13, 27],
                    color: COLOR_2
                },
                {
                    name: "PRODUCT C",
                    data: [11, 17, 15, 15, 21, 14],
                    color: COLOR_3
                },
                {
                    name: "PRODUCT D",
                    data: [21, 7, 25, 13, 22, 8],
                    color: COLOR_4
                }
            ],
            chart: {
                type: "bar",
                height: 350,
                stacked: true,
                toolbar: {
                    show: true
                },
                zoom: {
                    enabled: true
                }
            },
            responsive: [
                {
                    breakpoint: 480,
                    options: {
                        legend: {
                            position: "bottom",
                            offsetX: -10,
                            offsetY: 0
                        }
                    }
                }
            ],
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '20px'
                }
            },
            xaxis: {
                type: "category",
                categories: [
                    "01/2011",
                    "02/2011",
                    "03/2011",
                    "04/2011",
                    "05/2011",
                    "06/2011"
                ]
            },
            legend: {
                position: "right",
                offsetY: 40
            },
            fill: {
                opacity: 1
            }
        }
        new ApexCharts(document.querySelector("#stack-column-chart"), stackColumnOption).render();

        const basicBarOption = {
            series: [
                {
                    name: "basic",
                    data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380],
                    color: COLOR_1
                }
            ],
            chart: {
                ...ApexChartDefault,
                type: "bar",
                height: 350
            },
            plotOptions: {
                bar: {
                    horizontal: true
                }
            },
            dataLabels: ApexDataLabelDefault,
            xaxis: {
                categories: [
                    "South Korea",
                    "Canada",
                    "United Kingdom",
                    "Netherlands",
                    "Italy",
                    "France",
                    "Japan",
                    "United States",
                    "China",
                    "Germany"
                ]
            }
        }
        new ApexCharts(document.querySelector("#basic-bar-chart"), basicBarOption).render();

        const groupedBarOption = {
            series: [
                {
                    name: "serie1",
                    data: [44, 55, 41, 64, 22, 43, 21],
                    color: COLOR_1
                },
                {
                    name: "serie2",
 
                    data: [53, 32, 33, 52, 13, 44, 32],
                    color: COLOR_2
                }
            ],
            chart: {
                ...ApexChartDefault,
                type: "bar",
                height: 430
            },
            plotOptions: {
                bar: {
                    horizontal: true,
                    dataLabels: {
                        position: "top"
                    }
                }
            },
            dataLabels: {
                enabled: true,
                offsetX: -6,
                style: {
                    fontSize: "12px",
                    colors: ["#fff"]
                }
            },
            stroke: {
                show: true,
                width: 1,
                colors: ["#fff"]
            },
            xaxis: {
                categories: [2001, 2002, 2003, 2004, 2005, 2006, 2007]
            }
        }
        new ApexCharts(document.querySelector("#grouped-bar-chart"), groupedBarOption).render();
        
        const simplePieOption = {
            series: [44, 55, 13, 43, 22],
            chart: {
                ...ApexChartDefault,
                width: 380,
                type: "pie"
            },
            labels: ["Team A", "Team B", "Team C", "Team D", "Team E"],
            responsive: [
                {
                    breakpoint: 480,
                    options: {
                        chart: {
                            width: 200
                        },
                        legend: {
                            position: "bottom"
                        }
                    }
                }
            ]
        }
        new ApexCharts(document.querySelector("#simple-pie"), simplePieOption).render();

        const simpleDonutOption ={
            series: [44, 55, 13, 43, 22],
            chart: {
                ...ApexChartDefault,
                type: "donut"
            },
            labels: ["Team A", "Team B", "Team C", "Team D", "Team E"],
            responsive: [
                {
                    breakpoint: 480,
                    options: {
                        chart: {
                            width: 200
                        },
                        legend: {
                            position: "bottom"
                        }
                    }
                }
            ]
        }
        new ApexCharts(document.querySelector("#simple-donut"), simpleDonutOption).render();
    }
}

$(() => { Chart.init(); });

