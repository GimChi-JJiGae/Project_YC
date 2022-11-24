<template>
  <div>
    <h5>선호 장르 및 추천</h5>
    <Doughnut
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
    />
  </div>
  </template>
  
  <script>
  import { Doughnut } from 'vue-chartjs'
  
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    ArcElement,
    CategoryScale
  } from 'chart.js'
  
  ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)
  
  export default {
    name: 'DoughnutChart',
    components: {
      Doughnut
    },
    props: {
      movies: Array,
      chartData: Object,
      chartId: {
        type: String,
        default: 'doughnut-chart'
      },
      datasetIdKey: {
        type: String,
        default: 'label'
      },
      width: {
        type: Number,
        default: 400
      },
      height: {
        type: Number,
        default: 400
      },
      cssClasses: {
        default: '',
        type: String
      },
      styles: {
        type: Object,
        default: () => {}
      },
      plugins: {
        type: Array,
        default: () => []
      }
    },
    data() {
      return {
        chartOptions: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false,
            },
          },
          scales: {
            xAxes: [{
              stacked:true,
            }]
          },
        },
        lawData: {},
      }
    },
  }
  </script>
  <style>
  .dd{
    color: #3dda4a;
  }
  </style>