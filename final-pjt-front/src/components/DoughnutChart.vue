<template>
  <div>
    <h5>선호 장르</h5>
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
        chartData: {
          labels: ['VueJs', 'EmberJs', 'ReactJs', 'AngularJs'],
          datasets: [
            {
              backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
              data: [40, 20, 80, 10]
            }
          ]
        },
        chartOptions: {
          responsive: true,
          maintainAspectRatio: false
        }
      }
    },
    methods: {
      getData() {
        for (const movie of this.movies) {
          console.log(movie)
          console.log(movie.genres)
          console.log(movie.genre_name)
          // for (const genre of movie.genres) {
          //   if (this.chartData['labels'].includes(genre_set(genre))) {
          //     console.log()
          //   }
          // }
        }
      }
    },
    // computed: {
    //   ChartData() {
    //     this.getData()
    //   }
    // }
    created() {
      this.getData()
    }
  }
  </script>
  