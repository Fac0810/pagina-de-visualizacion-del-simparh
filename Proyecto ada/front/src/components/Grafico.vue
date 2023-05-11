<template>
    <div style="position: relative; height:80vh;">
      <Bar v-if="loaded" :data="chartData" :options="chartOptions"/>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  import { Bar } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  export default {
    name: 'BarChart',
    components: { Bar },
    data: () => ({
      loaded: false,
      options: null,
      dataName:'',
      chartData: [],
      data:[],
      label:[],
      chartOptions:{
        responsive: true,
        scales: {
          x: {
          title: {
            color: 'dark grey',
            display: true,
            text: 'Fecha'
            }
          },
          y: {
          title: {
            color: 'dark grey',
            display: true,
            text: 'Grados C°'
            }
          }
        }
      }
    }),
    async mounted () {
      this.loaded = false
      const mediciones = await axios.get('http://127.0.0.1:8000/api/v1.0/mediciones/');
      mediciones.data.map((row)=>(
        this.label.push(row.fecha),
        this.data.push(row.tmax)
      ))
      this.chartData = {
        labels: this.label,
        datasets:[
          {label:'Temperatura Max', data: this.data, backgroundColor:'blue'}
        ]
      };
      this.loaded = true;
    }
  }
  </script>
  