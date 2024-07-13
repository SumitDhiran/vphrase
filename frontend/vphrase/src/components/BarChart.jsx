import { React, useState, useEffect } from 'react';
import axios from 'axios';
import { Bar } from "react-chartjs-2";

import {
  Chart,
  ArcElement,
  LineElement,
  BarElement,
  PointElement,
  BarController,
  BubbleController,
  DoughnutController,
  LineController,
  PieController,
  PolarAreaController,
  RadarController,
  ScatterController,
  CategoryScale,
  LinearScale,
  LogarithmicScale,
  RadialLinearScale,
  TimeScale,
  TimeSeriesScale,
  Decimation,
  Filler,
  Legend,
  Title,
  Tooltip
} from 'chart.js';

Chart.register(
  ArcElement,
  LineElement,
  BarElement,
  PointElement,
  BarController,
  BubbleController,
  DoughnutController,
  LineController,
  PieController,
  PolarAreaController,
  RadarController,
  ScatterController,
  CategoryScale,
  LinearScale,
  LogarithmicScale,
  RadialLinearScale,
  TimeScale,
  TimeSeriesScale,
  Decimation,
  Filler,
  Legend,
  Title,
  Tooltip
);


const BarChart = ({year}) => {
  const [data, setData] = useState([]);

    useEffect(() => {
        axios.get(`http://localhost:8000/movies/bar_chart/?year=${year}`)
            .then(response => {console.log(response)
              setData(response.data)})
            .catch(error => console.error('Error fetching data', error));
    }, [year]);

    const chartData = {
        labels: data.map(movie => movie.movie),
        datasets: [
            {
                label: 'Gross',
                data: data.map(movie => movie.gross),
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
            },
        ],
    };

    return <Bar data={chartData} />;
}

export default BarChart;