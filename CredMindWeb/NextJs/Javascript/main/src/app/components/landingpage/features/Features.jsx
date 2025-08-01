'use client';
import React from 'react';
import FeaturesTitle from './FeaturesTitle';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import { Grid } from '@mui/material';
import Typography from '@mui/material/Typography';
import {
  IconAdjustments,
  IconArchive,
  IconArrowsShuffle,
  IconBook,
  IconBuildingCarousel,
  IconCalendar,
  IconChartPie,
  IconDatabase,
  IconDiamond,
  IconLanguageKatakana,
  IconLayersIntersect,
  IconMessages,
  IconRefresh,
  IconTag,
  IconWand,
  IconLockAccess,
  IconSquareKey,
  IconTable,
  IconPresentation,
  IconPackage
} from '@tabler/icons-react';
import AnimationFadeIn from '../animation/Animation';

const featuresData = [
  {
    icon: <IconWand width={40} height={40} strokeWidth={1.5} />,
    title: '6 Theme Colors',
    subtext: 'We have included 6 pre-defined Theme Colors with Elegant Admin.',
  },
  {
    icon: <IconArchive width={40} height={40} strokeWidth={1.5} />,
    title: '65+ Page Templates',
    subtext: 'Yes, we have 4 demos & 65+ Pages per demo to make it easier.',
  },
  {
    icon: <IconAdjustments width={40} height={40} strokeWidth={1.5} />,
    title: '45+ UI Components',
    subtext: 'Almost 45+ UI Components being given with Modernize Admin Pack.',
  },
  {
    icon: <IconPresentation width={40} height={40} strokeWidth={1.5} />,
    title: '4+ Frontend Pages',
    subtext: 'We have added useful frontend pages with Modernize Admin',
  },
  {
    icon: <IconPackage width={40} height={40} strokeWidth={1.5} />,
    title: 'Blogs with MDX',
    subtext: 'It provides a comprehensive blogging solution using MDX, which uniquely blends Markdown and JSX.',
  },
  {
    icon: <IconAdjustments width={40} height={40} strokeWidth={1.5} />,
    title: '45+ UI Components',
    subtext: 'Almost 45+ UI Components being given with Modernize Admin Pack.',
  },
  {
    icon: <IconTag width={40} height={40} strokeWidth={1.5} />,
    title: 'Material Ui',
    subtext: 'Its been made with Material Ui and full responsive layout.',
  },
  {
    icon: <IconLockAccess width={40} height={40} strokeWidth={1.5} />,
    title: 'Next-Auth',
    subtext: 'We have added Google, Github & Credential Provider with NextAuth ',
  },

  {
    icon: <IconSquareKey width={40} height={40} strokeWidth={1.5} />,
    title: 'Firebase',
    subtext: 'This template comes with Firebase implementation.',
  },
  {
    icon: <IconTable width={40} height={40} strokeWidth={1.5} />,
    title: 'React Table',
    subtext: 'Supercharge your tables or build a datagrid from scratch for TS/JS React.',
  },
  {
    icon: <IconDiamond width={40} height={40} strokeWidth={1.5} />,
    title: '3400+ Font Icons',
    subtext: 'Lots of Icon Fonts are included here in the package of Elegant Admin.',
  },
  {
    icon: <IconDatabase width={40} height={40} strokeWidth={1.5} />,
    title: 'SWR',
    subtext: 'SWR is a React hook for fetching and caching data efficiently.',
  },
  {
    icon: <IconLanguageKatakana width={40} height={40} strokeWidth={1.5} />,
    title: 'i18 React',
    subtext: 'react-i18 is a powerful internationalization framework for React.',
  },
  {
    icon: <IconBuildingCarousel width={40} height={40} strokeWidth={1.5} />,
    title: 'Slick Carousel',
    subtext: 'The Last React Carousel You will Ever Need!',
  },
  {
    icon: <IconArrowsShuffle width={40} height={40} strokeWidth={1.5} />,
    title: 'Easy to Customize',
    subtext: 'Customization will be easy as we understand your pain.',
  },
  {
    icon: <IconChartPie width={40} height={40} strokeWidth={1.5} />,
    title: 'Lots of Chart Options',
    subtext: 'You name it and we have it, Yes lots of variations for Charts.',
  },
  {
    icon: <IconLayersIntersect width={40} height={40} strokeWidth={1.5} />,
    title: 'Lots of Table Examples',
    subtext: 'Data Tables are initial requirement and we added them.',
  },
  {
    icon: <IconRefresh width={40} height={40} strokeWidth={1.5} />,
    title: 'Regular Updates',
    subtext: 'We are constantly updating our pack with new features.',
  },
  {
    icon: <IconBook width={40} height={40} strokeWidth={1.5} />,
    title: 'Detailed Documentation',
    subtext: 'We have made detailed documentation, so it will easy to use.',
  },
  {
    icon: <IconCalendar width={40} height={40} strokeWidth={1.5} />,
    title: 'Calendar Design',
    subtext: 'Calendar is available with our package & in nice design.',
  },
  {
    icon: <IconMessages width={40} height={40} strokeWidth={1.5} />,
    title: 'Dedicated Support',
    subtext: 'We believe in supreme support is key and we offer that.',
  },
];

const Features = () => {
  return (
    (<Box sx={{
      py: 6
    }}>
      <Container maxWidth="lg">
        <FeaturesTitle />
        <AnimationFadeIn>
          <Box sx={{
            mt: 6
          }}>
            <Grid container spacing={3}>
              {featuresData.map((feature, index) => (
                <Grid
                  key={index}
                  size={{
                    xs: 12,
                    sm: 4,
                    lg: 3
                  }}
                  sx={{
                    textAlign: "center"
                  }}>
                  <Box sx={{
                    color: "primary.main"
                  }}>{feature.icon}</Box>
                  <Typography variant="h5" sx={{
                    mt: 3
                  }}>
                    {feature.title}
                  </Typography>
                  <Typography
                    variant="subtitle1"
                    color="textSecondary"
                    sx={{
                      mt: 1,
                      mb: 3
                    }}>
                    {feature.subtext}
                  </Typography>
                </Grid>
              ))}
            </Grid>
          </Box>
        </AnimationFadeIn>
      </Container>
    </Box>)
  );
};

export default Features;
