import * as React from 'react';
import { Grid, Rating, Stack } from '@mui/material';
import Breadcrumb from '@/app/(DashboardLayout)/layout/shared/breadcrumb/Breadcrumb';
import PageContainer from '@/app/components/container/PageContainer';
import ParentCard from '@/app/components/shared/ParentCard';
import ChildCard from '@/app/components/shared/ChildCard';

import Controlled from '@/app/components/ui-components/rating/Controlled';
import ReadOnly from '@/app/components/ui-components/rating/ReadOnly';
import Disabled from '@/app/components/ui-components/rating/Disabled';
import NoRating from '@/app/components/ui-components/rating/NoRating';
import RatingPrecision from '@/app/components/ui-components/rating/RatingPrecision';
import HoverFeedback from '@/app/components/ui-components/rating/HoverFeedback';
import CustomIconSet from '@/app/components/ui-components/rating/CustomIconSet';
import RadioGroup from '@/app/components/ui-components/rating/RadioGroup';

const BCrumb = [
  {
    to: '/',
    title: 'Home',
  },
  {
    title: 'Rating',
  },
];

const MuiRating = () => {
  return (
    (<PageContainer title="Rating" description="this is Rating">
      {/* breadcrumb */}
      <Breadcrumb title="Rating" items={BCrumb} />
      {/* end breadcrumb */}
      <ParentCard title="Rating">
        <Grid container spacing={3}>
          <Grid
            size={{
              xs: 12,
              lg: 4,
              sm: 6
            }}
            sx={{
              display: "flex",
              alignItems: "stretch"
            }}>
            <Controlled />
          </Grid>
          <Grid
            size={{
              xs: 12,
              lg: 4,
              sm: 6
            }}
            sx={{
              display: "flex",
              alignItems: "stretch"
            }}>
            <ReadOnly />
          </Grid>
          <Grid
            size={{
              xs: 12,
              lg: 4,
              sm: 6
            }}
            sx={{
              display: "flex",
              alignItems: "stretch"
            }}>
            <Disabled />
          </Grid>
          <Grid
            size={{
              xs: 12,
              lg: 4,
              sm: 6
            }}
            sx={{
              display: "flex",
              alignItems: "stretch"
            }}>
            <NoRating />
          </Grid>
          <Grid
            size={{
              xs: 12,
              lg: 4,
              sm: 6
            }}
            sx={{
              display: "flex",
              alignItems: "stretch"
            }}>
            <RatingPrecision />
          </Grid>
          <Grid
            size={{
              xs: 12,
              lg: 4,
              sm: 6
            }}
            sx={{
              display: "flex",
              alignItems: "stretch"
            }}>
            <HoverFeedback />
          </Grid>

          <Grid
            size={{
              xs: 12,
              lg: 4,
              sm: 6
            }}
            sx={{
              display: "flex",
              alignItems: "stretch"
            }}>
            <CustomIconSet />
          </Grid>
          <Grid
            size={{
              xs: 12,
              lg: 4,
              sm: 6
            }}
            sx={{
              display: "flex",
              alignItems: "stretch"
            }}>
            <ChildCard title="10 Stars">
              <Rating name="customized-10" defaultValue={2} max={10} />
            </ChildCard>
          </Grid>
          <Grid
            size={{
              xs: 12,
              lg: 4,
              sm: 6
            }}
            sx={{
              display: "flex",
              alignItems: "stretch"
            }}>
            <RadioGroup />
          </Grid>
          <Grid
            size={{
              xs: 12,
              lg: 4,
              sm: 6
            }}
            sx={{
              display: "flex",
              alignItems: "stretch"
            }}>
            <ChildCard title="Sizes">
              <Stack spacing={2}>
                <Rating name="size-small" defaultValue={2} size="small" />
                <Rating name="size-medium" defaultValue={2} />
                <Rating name="size-large" defaultValue={2} size="large" />
              </Stack>
            </ChildCard>
          </Grid>
        </Grid>
      </ParentCard>
    </PageContainer>)
  );
};
export default MuiRating;
