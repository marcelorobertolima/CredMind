import { Grid } from '@mui/material';

// common component
import Breadcrumb from '@/app/(DashboardLayout)/layout/shared/breadcrumb/Breadcrumb';
import PageContainer from '@/app/components/container/PageContainer';
import ParentCard from '@/app/components/shared/ParentCard';

import TooltipSimple from '@/app/components/ui-components/tooltip/TooltipSimple';
import TooltipArrow from '@/app/components/ui-components/tooltip/TooltipArrow';
import TooltipVariableWidth from '@/app/components/ui-components/tooltip/TooltipVariableWidth';
import TooltipTransition from '@/app/components/ui-components/tooltip/TooltipTransition';
import TooltipPosition from '@/app/components/ui-components/tooltip/TooltipPosition';

const BCrumb = [
  {
    to: '/',
    title: 'Home',
  },
  {
    title: 'Tooltip',
  },
];


const MuiTooltip = () => (
  <PageContainer title="Tooltip" description="this is Tooltip">
    {/* breadcrumb */}
    <Breadcrumb title="Tooltip" items={BCrumb} />
    {/* end breadcrumb */}

    <ParentCard title="Tooltip">
      <Grid container spacing={3}>
        <Grid
          size={{
            xs: 12,
            sm: 6
          }}
          sx={{
            display: "flex",
            alignItems: "stretch"
          }}>
          <TooltipSimple />
        </Grid>
        <Grid
          size={{
            xs: 12,
            sm: 6
          }}
          sx={{
            display: "flex",
            alignItems: "stretch"
          }}>
          <TooltipArrow />
        </Grid>

        <Grid
          size={{
            xs: 12,
            sm: 6
          }}
          sx={{
            display: "flex",
            alignItems: "stretch"
          }}>
          <TooltipVariableWidth />
        </Grid>

        <Grid
          size={{
            xs: 12,
            sm: 6
          }}
          sx={{
            display: "flex",
            alignItems: "stretch"
          }}>
          <TooltipTransition />
        </Grid>
        <Grid
          size={12}
          sx={{
            display: "flex",
            alignItems: "stretch"
          }}>
          <TooltipPosition />
        </Grid>
      </Grid>
    </ParentCard>
  </PageContainer>
);
export default MuiTooltip;
