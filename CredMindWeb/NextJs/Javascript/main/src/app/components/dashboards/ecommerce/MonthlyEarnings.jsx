'use client';
import React from "react";
import dynamic from "next/dynamic";
const Chart = dynamic(() => import("react-apexcharts"), { ssr: false });
import { useTheme } from "@mui/material/styles";
import { Stack, Typography, Avatar, Box } from "@mui/material";
import { IconArrowUpLeft } from "@tabler/icons-react";

import DashboardCard from "../../shared/DashboardCard";
import SkeletonMonthlyEarningsCard from "../skeleton/MonthlyEarningsCard";


const MonthlyEarnings = ({ isLoading }) => {
  // chart color
  const theme = useTheme();
  const primary = theme.palette.primary.main;
  const primarylight = theme.palette.primary.light;
  const successlight = theme.palette.success.light;

  // chart
  const optionscolumnchart = {
    chart: {
      type: "area",
      fontFamily: "'Plus Jakarta Sans', sans-serif;",
      foreColor: "#adb0bb",
      toolbar: {
        show: false,
      },
      height: 70,
      sparkline: {
        enabled: true,
      },
      group: "sparklines",
    },
    stroke: {
      curve: "smooth",
      width: 2,
    },
    fill: {
      colors: [primarylight],
      type: "solid",
      opacity: 0.05,
    },
    markers: {
      size: 0,
    },
    tooltip: {
      theme: theme.palette.mode === "dark" ? "dark" : "light",
      x: {
        show: false,
      },
    },
  };
  const seriescolumnchart = [
    {
      name: "",
      color: primary,
      data: [25, 66, 20, 40, 12, 58, 20],
    },
  ];

  return (<>
    {
      isLoading ? (
        <SkeletonMonthlyEarningsCard />
      ) : (
        <DashboardCard
          title="Monthly Earnings"
          action={
            <Avatar
              variant="rounded"
              sx={{
                bgcolor: (theme) => theme.palette.primary.light,
                width: 40,
                height: 40,
              }}
            >
              <Avatar
                src="/images/svgs/icon-master-card-2.svg"
                alt="icon"
                sx={{ width: 24, height: 24 }}
              />
            </Avatar>
          }
          footer={
            <Box sx={{
              height: "70px"
            }}>
              <Chart
                options={optionscolumnchart}
                series={seriescolumnchart}
                type="area"
                width={"100%"}
                height="70px"
              />
            </Box>
          }
        >
          <>
            <Stack
              direction="row"
              spacing={1}
              sx={{
                alignItems: "center",
                mb: 3
              }}>
              <Typography variant="h3" sx={{
                fontWeight: "700"
              }}>
                $6,820
              </Typography>
              <Stack
                direction="row"
                spacing={1}
                sx={{
                  mt: 1,
                  mb: 2,
                  alignItems: "center"
                }}>
                <Avatar sx={{ bgcolor: successlight, width: 20, height: 20 }}>
                  <IconArrowUpLeft width={18} color="#13DEB9" />
                </Avatar>
                <Typography variant="subtitle2" color="textSecondary">
                  +9%
                </Typography>
              </Stack>
            </Stack>
          </>
        </DashboardCard>
      )}
  </>);
};

export default MonthlyEarnings;
