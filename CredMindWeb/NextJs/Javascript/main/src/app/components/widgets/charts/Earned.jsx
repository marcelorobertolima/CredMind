'use client'
import dynamic from 'next/dynamic';
const Chart = dynamic(() => import('react-apexcharts'), { ssr: false });
import { useTheme } from '@mui/material/styles';
import { CardContent, Typography } from '@mui/material';
import BlankCard from '../../shared/BlankCard';
import { Stack } from '@mui/system';

const Earned = () => {
  // chart color
  const theme = useTheme();
  const primary = theme.palette.primary.main;

  // chart
  const optionscolumnchart = {
    chart: {
      type: 'area',
      fontFamily: "'Plus Jakarta Sans', sans-serif;",
      foreColor: '#adb0bb',
      toolbar: {
        show: false,
      },
      height: 90,
      sparkline: {
        enabled: true,
      },
    },
    colors: [primary],

    stroke: {
      curve: 'straight',
      width: 2,
    },
    dataLabels: {
      enabled: false,
    },
    legend: {
      show: false,
    },
    grid: {
      show: false,
    },
    xaxis: {
      axisBorder: {
        show: true,
      },
      axisTicks: {
        show: false,
      },
    },
    tooltip: {
      theme: theme.palette.mode === 'dark' ? 'dark' : 'light',
      fillSeriesColor: false,
    },
  };
  const seriescolumnchart = [
    {
      name: '',
      data: [0, 3, 1, 2, 8, 1, 5, 1],
    },
  ];

  return (
    (<BlankCard>
      <CardContent sx={{ p: '30px' }}>
        <Typography variant="h4">2,545</Typography>
        <Stack direction="row" spacing={2} sx={{
          justifyContent: "space-between"
        }}>
          <Typography variant="subtitle2" color="textSecondary">
            Earned
          </Typography>
          <Typography variant="subtitle2" sx={{
            color: "success.main"
          }}>
            +1.20%
          </Typography>
        </Stack>
      </CardContent>
      <Chart
        options={optionscolumnchart}
        series={seriescolumnchart}
        type="area"
        height="90px"
        width={'100%'}
      />
    </BlankCard>)
  );
};

export default Earned;
