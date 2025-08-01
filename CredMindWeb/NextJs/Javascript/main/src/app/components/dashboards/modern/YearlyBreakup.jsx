'use client';
import dynamic from 'next/dynamic';
const Chart = dynamic(() => import('react-apexcharts'), { ssr: false });
import { useTheme } from '@mui/material/styles';
import { Grid, Stack, Typography, Avatar } from '@mui/material';
import { IconArrowUpLeft } from '@tabler/icons-react';

import DashboardCard from '../../shared/DashboardCard';
import SkeletonYearlyBreakupCard from '../skeleton/YearlyBreakupCard';

const YearlyBreakup = ({ isLoading }) => {
  // chart color
  const theme = useTheme();
  const primary = theme.palette.primary.main;
  const primarylight = theme.palette.primary.light;
  const successlight = theme.palette.success.light;

  // chart
  const optionscolumnchart = {
    chart: {
      type: 'donut',
      fontFamily: "'Plus Jakarta Sans', sans-serif;",
      foreColor: '#adb0bb',
      toolbar: {
        show: false,
      },
      height: 155,
    },
    colors: [primary, primarylight, '#F9F9FD'],
    plotOptions: {
      pie: {
        startAngle: 0,
        endAngle: 360,
        donut: {
          size: '75%',
          background: 'transparent',
        },
      },
    },
    tooltip: {
      theme: theme.palette.mode === 'dark' ? 'dark' : 'light',
      fillSeriesColor: false,
    },
    stroke: {
      show: false,
    },
    dataLabels: {
      enabled: false,
    },
    legend: {
      show: false,
    },
    responsive: [
      {
        breakpoint: 991,
        options: {
          chart: {
            width: 120,
          },
        },
      },
    ],
  };
  const seriescolumnchart = [38, 40, 25];

  return (<>
    {isLoading ? (
      <SkeletonYearlyBreakupCard />
    ) : (
      <DashboardCard title="Yearly Breakup">
        <Grid container spacing={3}>
          {/* column */}
          <Grid
            size={{
              xs: 7,
              sm: 7
            }}>
            <Typography variant="h3" sx={{
              fontWeight: "700"
            }}>
              $36,358
            </Typography>
            <Stack
              direction="row"
              spacing={1}
              sx={{
                mt: 1,
                alignItems: "center"
              }}>
              <Avatar sx={{ bgcolor: successlight, width: 27, height: 27 }}>
                <IconArrowUpLeft width={20} color="#39B69A" />
              </Avatar>
              <Typography variant="subtitle2" sx={{
                fontWeight: "600"
              }}>
                +9%
              </Typography>
              <Typography variant="subtitle2" color="textSecondary">
                last year
              </Typography>
            </Stack>
            <Stack spacing={3} direction="row" sx={{
              mt: 5
            }}>
              <Stack direction="row" spacing={1} sx={{
                alignItems: "center"
              }}>
                <Avatar
                  sx={{ width: 9, height: 9, bgcolor: primary, svg: { display: 'none' } }}
                ></Avatar>
                <Typography variant="subtitle2" color="textSecondary">
                  2025
                </Typography>
              </Stack>
              <Stack direction="row" spacing={1} sx={{
                alignItems: "center"
              }}>
                <Avatar
                  sx={{ width: 9, height: 9, bgcolor: primarylight, svg: { display: 'none' } }}
                ></Avatar>
                <Typography variant="subtitle2" color="textSecondary">
                  2025
                </Typography>
              </Stack>
            </Stack>
          </Grid>
          {/* column */}
          <Grid
            size={{
              xs: 5,
              sm: 5
            }}>
            <Chart
              options={optionscolumnchart}
              series={seriescolumnchart}
              type="donut"
              height={150}
              width={'100%'}
            />
          </Grid>
        </Grid>
      </DashboardCard>
    )}
  </>);
};

export default YearlyBreakup;
