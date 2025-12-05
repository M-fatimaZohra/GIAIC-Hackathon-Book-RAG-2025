import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [    'course-details',
    'module1-overview',
    'module2-overview',
    'module3-overview',
    'module4-overview',
    {

      type: 'category',
      label: 'Modules',
      items: [
        'module1/module1',
        'module2/module2',
        'module3/module3',
        'module4/module4',
        'module5/module5',
        'module6/module6',
      ],
    },
    'weekly-breakdown',
    'assessments',
    'hardware-requirements',
    'robot-lab',
    'cloud-lab',
    'student-kits',    {
      type: 'category',
      label: 'Appendices',
      items: [
        'appendices/sensors',
        'appendices/robotics-math',
        'appendices/glossary',
        'appendices/hardware-setup',
      ],
    },  ],
};

export default sidebars;
