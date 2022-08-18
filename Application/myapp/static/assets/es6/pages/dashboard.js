import { 
    ApexChartDefault,  
    ApexBarDefault, 
    ApexDataLabelDefault,
    ApexStrokeDefault,
    ApexColorDefault,
    COLOR_1,
    COLOR_2,
    COLOR_3,
    COLOR_4
} from '../constant/chart.constant';
import * as am4core from '../../../../node_modules/@amcharts/amcharts4/core';
import * as am4maps from '../../../../node_modules/@amcharts/amcharts4/maps';
import am4geodata_usaLow from '../../../../node_modules/@amcharts/amcharts4-geodata/usaLow';
import am4themes_animated from '../../../../node_modules/@amcharts/amcharts4/themes/animated';

const regionData = [
    {
        id: 'US-TX',
        name: 'Texas',
        value: 4447100,
        fill: COLOR_1
    },
    {
        id: 'US-GA',
        name: 'Georgia',
        value: 626932,
        fill: COLOR_2
    },
    {
        id: 'US-UT',
        name: 'Utah',
        value: 5130632,
        fill: COLOR_3
    },
    {
        id: 'US-NE',
        name: 'Nebraska',
        value: 5130632,
        fill: COLOR_4
    },
]

class Dashboard {

    static init() {

        const monthlyRevenueOptions = {
            series: [
                {
                    name: 'Revenue',
                    data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
                }
            ],
            chart: {
                ...ApexChartDefault,
                type: 'bar',
                height: 100,
                sparkline: {
                    enabled: true
                },
            },
            plotOptions: ApexBarDefault,
            dataLabels: ApexDataLabelDefault,
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            xaxis: {
                categories: ['Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct']
            },
            yaxis: {
                title: {
                    text: '$ (thousands)'
                }
            },
            fill: {
                opacity: 1
            },
            tooltip: {
                y: {
                    formatter: function(val) {
                        return '$ ' + val + ' thousands';
                    }
                }
            }
        }
          
        const monthlyRevenueChart = new ApexCharts(document.querySelector("#monthly-revenue"), monthlyRevenueOptions);

        monthlyRevenueChart.render();


        am4core.useTheme(am4themes_animated);

        let chart = am4core.create("region-data-map", am4maps.MapChart);

        chart.geodata = am4geodata_usaLow;
        chart.projection = new am4maps.projections.AlbersUsa();

        let polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
        let polygonTemplate = polygonSeries.mapPolygons.template;

        polygonTemplate.tooltipText = '{name}: {value}';
        polygonTemplate.nonScalingStroke = true;
        polygonTemplate.strokeWidth = 2;
        polygonTemplate.stroke = am4core.color('#bfd4e0')
        polygonTemplate.propertyFields.fill = 'fill';
        polygonTemplate.fill = am4core.color('#fff')

        polygonSeries.data = [...regionData]

        polygonSeries.useGeodata = true;

        const regionDataOptions = {
            series: [],
            chart: {
                ...ApexChartDefault,
                type: 'donut'
            },
            labels: [],
            legend: {
                show: false,
            },
            dataLabels: {
                enabled: false
            },
            plotOptions: {
                pie: {
                    donut: {
                        size: '75%'
                    }
                }
            },
            colors: [ COLOR_1, COLOR_2, COLOR_3, COLOR_4]
        }

        regionData.forEach((elm, i) => {
            regionDataOptions.series.push(elm.value)
            regionDataOptions.labels.push(elm.id)
        })
          
        const regionDataChart = new ApexCharts(document.querySelector("#region-data-chart"), regionDataOptions);

        regionDataChart.render();


        const overviewChartOptions = {
            series: [
                {
                    name: 'Income',
                    data: [3572, 4121, 6261, 4231, 1332, 1844, 2980, 3759, 3632, 5157, 3245, 3535],
                },
                {
                    name: 'Expense',
                    data: [4555, 5232, 3812, 2486, 3319, 2643, 2111, 2046, 629, 831, 1525, 1088],
                }
            ],
            chart: {
                ...ApexChartDefault,
                height: 330,
                type: 'line'
            },
            dataLabels: ApexDataLabelDefault,
            stroke: {
                ...ApexStrokeDefault,
                dashArray: [0, 8, 5]
            },
            color: ApexColorDefault,
            legend: {
                tooltipHoverFormatter: function(val, opts) {
                    return (
                        `${val} - <strong>$${opts.w.globals.series[opts.seriesIndex][opts.dataPointIndex]} </strong>`                  
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
                categories: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            },
            tooltip: {
                y: [
                    {
                        title: {
                            formatter: (val) => val
                        }
                    },
                    {
                        title: {
                            formatter: (val) => val
                        }
                    },
                    {
                        title: {
                            formatter: function(val) {
                                return `$${val}`;
                            }
                        }
                    }
                ]
            }
        }

        const overviewChart = new ApexCharts(document.querySelector("#overview-chart"), overviewChartOptions);

        overviewChart.render();
    }
}

$(() => { Dashboard.init(); });

