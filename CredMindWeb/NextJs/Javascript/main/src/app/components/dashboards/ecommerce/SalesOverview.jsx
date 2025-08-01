'use client';
import React from 'react';
import dynamic from "next/dynamic";
const Chart = dynamic(() => import("react-apexcharts"), { ssr: false });
import { useTheme } from '@mui/material/styles';
import { Stack, Typography, Box } from '@mui/material';
import { IconGridDots } from '@tabler/icons-react';
import DashboardCard from '../../shared/DashboardCard';
import SkeletonSalesOverviewCard from '../skeleton/SalesOverviewCard';


const SalesOverview = ({ isLoading }) => {
  // chart color
  const theme = useTheme();
  const primary = theme.palette.primary.main;
  const secondary = theme.palette.secondary.main;
  const primarylight = theme.palette.primary.light;
  const textColor = theme.palette.mode === 'dark' ? 'rgba(255,255,255,0.8)' : '#2A3547';

  // chart
  const optionscolumnchart = {
    chart: {
      type: 'donut',
      fontFamily: "'Plus Jakarta Sans', sans-serif;",

      toolbar: {
        show: false,
      },
      height: 275,
    },
    labels: ["Profit", "Revenue", "Expance"],
    colors: [primary, primarylight, secondary],
    plotOptions: {
      pie: {

        donut: {
          size: '89%',
          background: 'transparent',

          labels: {
            show: true,
            name: {
              show: true,
              offsetY: 7,
            },
            value: {
              show: false,
            },
            total: {
              show: true,
              color: textColor,
              fontSize: '20px',
              fontWeight: '600',
              label: '$500,458',
            },
          },
        },
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      show: false,
    },
    legend: {
      show: false,
    },
    tooltip: {
      theme: theme.palette.mode === 'dark' ? 'dark' : 'light',
      fillSeriesColor: false,
    },
  };
  const seriescolumnchart = [55, 55, 55];

  return (<>
    {
      isLoading ? (
        <SkeletonSalesOverviewCard />
      ) : (
        <DashboardCard title="Sales Overview" subtitle="Every month">
          <>
            <Box
              sx={{
                mt: 3,
                height: "255px"
              }}>
              <Chart
                options={optionscolumnchart}
                series={seriescolumnchart}
                type="donut"
                height="275px"
                width={"100%"}
              />
            </Box>

            <Stack
              direction="row"
              spacing={2}
              sx={{
                justifyContent: "space-between",
                mt: 7
              }}>
              <Stack direction="row" spacing={2} sx={{
                alignItems: "center"
              }}>
                <Box
                  sx={{
                    width: 38,
                    height: 38,
                    bgcolor: "primary.light",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center"
                  }}>
                  <Typography
                    sx={{
                      color: "primary.main",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center"
                    }}>
                    <IconGridDots width={22} />
                  </Typography>
                </Box>
                <Box>
                  <Typography variant="h6" sx={{
                    fontWeight: "600"
                  }}>
                    $23,450
                  </Typography>
                  <Typography variant="subtitle2" color="textSecondary">
                    Profit
                  </Typography>
                </Box>
              </Stack>
              <Stack direction="row" spacing={2} sx={{
                alignItems: "center"
              }}>
                <Box
                  sx={{
                    width: 38,
                    height: 38,
                    bgcolor: "secondary.light",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center"
                  }}>
                  <Typography
                    sx={{
                      color: "secondary.main",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center"
                    }}>
                    <IconGridDots width={22} />
                  </Typography>
                </Box>
                <Box>
                  <Typography variant="h6" sx={{
                    fontWeight: "600"
                  }}>
                    $23,450
                  </Typography>
                  <Typography variant="subtitle2" color="textSecondary">
                    Expance
                  </Typography>
                </Box>
              </Stack>
            </Stack>
          </>
        </DashboardCard>
      )}
  </>);
};

export default SalesOverview;
